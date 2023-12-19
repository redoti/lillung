from flask import Flask, render_template, request, redirect, url_for
from keras.models import load_model
import tensorflow as tf
import numpy as np
import os
from scrapper import scrape_news

app = Flask(__name__,static_url_path='/', static_folder='/')

# Load the model
model_path = 'model\Resnet50.h5'
model = load_model(model_path)

@app.route('/')
def home():
    try:
        # Get the scraped news
        news_list = scrape_news()
        return render_template('index.html', news_list=news_list)
    except Exception as e:
        return str(e), 500  # Return the error message with a 500 status code

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        # Get the image file from the request
        file = request.files['file']

        # Use the original filename to save the file locally in the 'uploads' folder
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Preprocess the image
        img = tf.keras.utils.load_img(file_path, target_size=(256, 256))  # Resize to 256
        img_array = tf.keras.utils.img_to_array(img)  # Convert to array
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions
        img_array /= 255.0  # Normalize [0-1]

        # Make predictions
        predictions = model.predict(img_array)

        # Process predictions
        class_idx = np.argmax(predictions[0])
        classes = ["NORMAL", "PNEUMONIA", 'NOT XRAY']
        predicted_class = classes[class_idx]
        print(predicted_class)
        
        if predicted_class == 'NORMAL' or predicted_class == 'PNEUMONIA':

            # Rename the file based on the predicted class
            new_filename = f"{predicted_class}_{file.filename}"
            new_file_path = os.path.join('uploads', new_filename)

            # Check if a file with the same name already exists, and if it does, replace it
            if os.path.exists(new_file_path):
                os.remove(new_file_path)

            os.rename(file_path, new_file_path)

            result = {
                "prediction": predicted_class,
                "confidence": float(predictions[0][class_idx]),
                "filename": new_filename,
                "img_source": new_file_path
            }

            return render_template('result.html', result=result)
        else:
            result = {
                "prediction": predicted_class,
                "confidence": float(predictions[0][class_idx]),
                
            }
            
            return render_template('result.html', result=result)

    except Exception as e:
        return render_template('result.html', result={"error": str(e)})
    
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('predict'))

if __name__ == '__main__':
    app.run(debug=True)
