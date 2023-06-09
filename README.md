# Captstone-AzureML-MLEngineer-Nanodegree


# PIMA diabetes classification

 The goal of this project is to classify whether a female person has diabetes or not. This is a binary classification problem. 

## Project Set Up and Installation
1) Upload the pima_diabetes.csv file in the Data section of AzureML as a tabular file.
2)  Name of the data asset should be pima-diabetes
3) The AutoML run can be run by just running the automl.ipynb notebook. For querying the deployed model HTTP endpoint, use the endpoint.py script. Details on Model HTTP endpoint querying are provided later
4) The conda_dependencies.yml file should be present in Azure file system when running the hyperdrive run run in the hyperparameter_tuning.ipynb notebook


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
The below points describe the AutoML configuration which is set using the AutoMLConfig() in the code
1) experiment_timeout_minutes=30, maximum time upto which the AutoML run will continue. Helps in reducing unneccessary use of cluster time

2) task='classification', the task is to clasify whether a person has diabetes or not

3) primary_metric='accuracy', The metric being tracked is Accuracy since this a binary classification problem

4) training_data=train_ds, training_needs the dataset whihc has to be loaded before it is passed to AutoML Config

5) label_column_name='Outcome', 'Outcome' is the  name of the column in the dataset which is the target column to be predicted

6) n_cross_validations=5, number of cross validations ot perform to get the metric

7) compute_target = cpu_cluster, the compute target needs to be passed hte compute cluster whihc is created in the code

### Results
The AutoML model provided a best accuracy of around 0.78. The Voting Ensemble model which was a ensemble of different models like Logistic regression, XGBoostClassifier, RandomForestClassifier etc. There were different models of a single type in the ensemble with different hyperparameters. each model had a weight assigned to it and a scaling technique for preprocessing the data. More details about the model can be obtained in the automl.ipynb notebook

Logistic regression was the best performing model in terms of accuracy. The XGBoost classifier models were second. Thereafter, other models like LIghtGBM, RandomForestClassifier, ExtremeRandomTrees followed in terms of accuracy

##### Performance of various models produced by AutoML
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/a99c10e7-a50d-4b25-b7d3-57f11adeeca4)


##### RunDetails widget showing progess of AutoML
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/1fd419df-1227-486e-befa-ddc7f02c8bed)

##### Accuracy of Different AutoML models
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/0d4b6521-2964-46c5-a278-73f3bcfd0857)

##### Best AutoML model run ID 
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/8e66a78c-350c-421f-935c-5b3636c55120)

##### Best AutoML model description
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/3d8c663a-1739-46fc-963e-44a0bd036ebf)

##### Best AutoML model accuracy
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/7f7e84c4-8fe0-41d2-8b5a-8817b90231a9)

##### Best AutoML model i.e. Voting Ensemble cosntituent models and their weights
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/dc098a05-3760-4f86-90a9-b05b5d5afedc)

##### Best AutoML model metrics
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/5f575cd7-096d-4312-a378-1bbf14b92c81)


##### Deployed model screenshot from AzureML UI
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/ff89103e-4eed-4cc6-b8d2-9fcbfab2bcc1)

##### Call to the deployed model endpoint using endpoint.py and returned result from model
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/84ec562a-cb11-4da9-8fd8-d148091a9ace)



## Hyperparameter Tuning

Logistic regression model was chosen because of this being a binary classfication task. The hyperparameters being optimized were inverse regularization strength 'C' and number of iterations 'iter'. The C parameters was varied in the range 0.1 to 0.4 and the number of iteratins were chosen randomly from 12,25 and 50


### Results

The max accuracy was around 0.75. The parameters were C=0.349 and iter=50. Regularization strength reduces the overfitting tendency and number of iterations gives time to the gradient descent optimization in hte logistics regression loss function minimization. These are the reasons behind choosing these 2 hyperparameters.

Increasing the number of iterations could increase the model performance because it can be seen in the screenshots that the highest accuracy was observed of iterations=50. The effect of C on accuracy is not very evident from the results bu the range of C can be increased nevertheelsess from 0 to 1 to check performance. Also,  techniques like Bayesian parameter sampling which take into account the previous explored hyperparameters to reduce wasteful search can improve the hyperparameter optimization. 

##### Accuracy of different runs in Hyperdrive run
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/a0198ba6-81bb-4b4d-9993-9f54986981b5)

##### Run Details widget showing status of HyperDrive Run
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/874a8966-be3a-4a5b-ae64-54807f0788ba)

##### Accuracy metrics and and their respective parameters for HyperDrive run
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/7a870b5f-d357-4daa-acf9-0f52b2299560)

##### Best Run ID and the accuracy of the run
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/e45ee0ed-ce66-4952-bf47-d9cb5d88527f)

## Model Deployment

The deployed model is the VotingEnsemble produced by AutoML since it had a higher accuracy of 0.78.

The below mentioned process describes the model query procedure

1) The endpoint.py script is used for querying the model HTTP endpoint
2) Copy the REST endpoint and the primary key from the Endpoints -> Select Model -> Consume page in AzureML UI and paste them in the endpoint.py scoring_uri and key respectively
3) Change the data format in the endpoint.py as per the columns in the datset. The format of the dat can also be checked in the Consume page mentioned in Point 2
4) Open a Terminal window in AzureML and run python endpoint.py in the teminal
5) The results of the data query sent are displayed in the terminal

## Screen Recording
The video shows the deployed Voting Ensemble model HTTP endpoint query procedure using the endpoint.py script
[https://youtu.be/-eC-X_bmFOs](https://youtu.be/KYXcdR8ppfM)

## Project Improvements
Exploratory data analysis to check for features which are having some correlations with the predicted variable using chi square tests will help in choosing important features. Increasing the timeout of AutoML might help in exploring a wider range of models.
For Hyperdrive, increasing the number of iterations could increase the model performance because it can be seen in th escreenshots that the highest accuracy was observed of iterations=50. The effect of C on accuracy is not very evident from the results bu the range of C can be increased nevertheelsess from 0 to 1 to check performance. Also,  techniques like Bayesian parameter sampling which take into account the previous explored hyperparameters to reduce wasteful search can improve the hyperparameter optimization. 

