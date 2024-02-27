# Introduction

LilLung is a simple deep learning web application that containing and using dataset from [Kaggle](https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images) to do image classification Pediatric Pneumonia (1 - 5 years old children).

![img](https://i.imgur.com/asqhMdT.png)

# Environment Setup

Install fundamental environments including conda, python and the rest of package
 
### Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

```javascripts
https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
```

### Download Source Code

Open your terminal and run the following command or just download the `zip file`. My model that you can download it [here](https://drive.google.com/file/d/165eDzMkClIA7hufoXtlA0zx3KddnyYGE/view?usp=drive_link).
Make new folder named 'model' and place the model to that folder, it will looks like `lillung\model\Resnet50.h5`.
```javascripts
git clone https://github.com/redoti/lillung.git
```

### Create new python environment 

#### Run this command inside anaconda prompt

```javascripts
conda create -n lillungENV python=3.10
```

#### Activate our new environment

```javascripts
conda activate lillungENV
```

# Deploy the Source Code 
Before running anything, you'll need to install the python library package. Make sure your terminal active on project directory
```javascripts
pip install -r requirements.txt
```
### Running the interface locally
Run on `development environment` if you want to deploy the source code directly to the `development server`. Navigate to [http://127.0.0.1:5000/].
```javascripts
flask run
```

# Preview

### Result Pneumonia 
![img](https://i.imgur.com/Kv9M4kq.png)

### Result Normal
![img](https://i.imgur.com/80Ga7pw.png)

### Result Non Chest-Xray
![img](https://i.imgur.com/gtBf9lr.png)
