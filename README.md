# Introduction

LilLung is a simple machine learning web application that containing and using dataset from [Kaggle](https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images) to do image classification Pediatric Pneumonia (1 - 5 years old children).

![img](https://cdn.discordapp.com/attachments/994806484942721025/1186582967259242526/Screenshot_26.png?ex=6593c681&is=65815181&hm=31a406660b84dd9d459d949bfc699a46b52c88a733e44b125e51b9119c47a88f&)

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
![img](https://cdn.discordapp.com/attachments/994806484942721025/1186563229963526184/Screenshot_15.png?ex=6593b41f&is=65813f1f&hm=52e29b5136ef953c5ccda69127ad2b4a0001e628d5274cf774ac20f6bc4d69f7&)

### Result Normal
![img](https://cdn.discordapp.com/attachments/994806484942721025/1186563230622027806/Screenshot_16.png?ex=6593b41f&is=65813f1f&hm=9bfb4718b7b3bb8196612a7b0f4340f24a6f45af753eb7fd72d9ac379fb9f5af&)

### Result Non Chest-Xray
![img](https://cdn.discordapp.com/attachments/994806484942721025/1186563230961762364/Screenshot_17.png?ex=6593b41f&is=65813f1f&hm=75cf50e257580e43321d596bed58d38a7981fbf02edf7f2213cc7578409eebd1&)
