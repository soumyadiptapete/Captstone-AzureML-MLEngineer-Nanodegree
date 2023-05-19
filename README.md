# Captstone-AzureML-MLEngineer-Nanodegree


# PIMA diabetes classification

 The goal of this project is to classify whether a female person has diabetes or not. This is a binary classification problem. 

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset
The pima_diabetes.csv file contains the 8 input features for the classification problem. The target column is 'Outcome' which is 1 when the person has diabetes and 0 when they don't have diabetes. The features are number of pregnancies, glcucose concentration, blood pressure, skin fold thickness, serum insulin, BMI, diabetes pedigree function and age

### Overview
https://github.com/npradaschnor/Pima-Indians-Diabetes-Dataset is the link from where the data was obtained. This dataset is compiled by the National Institute of Diabetes and Digestive and Kidney Diseases. All the observations inthe dataset are for females above 21 years of age. For each obsrvation, a number of descriptors which are diagnostic test results and medical history information is given and also whether the person has diabetes or not is provided.

### Task
The task is to predict whether a person has diabetes or not based on the features provided in the dataset. there are total 8 features described previously.

### Access
The csv file is uploaded in the Data section of AzureML as a Tabular file. Then, the datset can be consumed by using the dataset name.
train_ds = Dataset.get_by_name(ws, name='pima-diabetes') where ws is ithe workspace

## Automated ML
experiment_timeout_minutes=30, maximum time upto whihc the AutoML run will continue
task='classification', the task is to clasify whether a person has diabetes or not
primary_metric='accuracy', The metric being tracked is Accuracy
training_data=train_ds, train_ds is the training dataset
label_column_name='Outcome', 'Outcome' is the column in the dataset whihc is the target column to be predicted
n_cross_validations=5, number of cross validations ot perform to get the metric
compute_target = cpu_cluster, the compute cluster whihc has been created in the code

### Results
The AutoML model provided a best accuracy of around 0.78. The Voting Ensemble model which was a ensemble of 26 models like Logistic regression, XGBoostClassifier, RandomForestClassifier etc. There wany different models of a single type inthe ensemble with different hyperparameters. each model had a weight assigned to it and a scaling technique for preprocessing the data. More details about the model can be obtained in the automl.ipynb notebook

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.


## Hyperparameter Tuning

Logistic regression model was chosen because of this being a binary classfication task. The hyperparameters being optimized were inverse regularization strength 'C' and number of iterations 'iter'. The C paramters was varied in the range 0.1 to 0.4 and the number of iteratins were chosen randomly from 12,25 and 50


### Results

the max accuracy was around 0.75. The parameters were C=0.349 and iter=50. Increasing the number of iterations could increase the model performance. Also,  techniques like Bayesian parameter sampling which take into account the previous explored hyperparameters to reduce wasteful search can improve the hyperparameter optimization. 

*TODO* Remember to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment

The deployed model is the VotingEnsemble produced by AutoML since it had a higher accuracy of 0.78.

The below code snippet gives a breakdown of model query procedure

service_name = 'automl-best-model1', get the name of the deployed endpoint

service = Webservice(ws, name=service_name), intialize the Webservice

input_data = {
    'data': [
        {'Pregnancies': 6, 'Glucose': 8, 'BloodPressure':72, 'SkinThickness':35, 'Insulin':0,
    'BMI':33.6,'DiabetesPedigreeFunction':0.627,'Age':50}  
    ]
}, create input data that will be sent to the model

input_data_json = json.dumps(input_data), convert input data to json format

output = service.run(input_data_json), send the json to the service initalized before. Output is the model prediction

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
https://youtu.be/-eC-X_bmFOs


## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
