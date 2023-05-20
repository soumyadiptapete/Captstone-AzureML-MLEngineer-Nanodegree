# Captstone-AzureML-MLEngineer-Nanodegree


# PIMA diabetes classification

 The goal of this project is to classify whether a female person has diabetes or not. This is a binary classification problem. 

## Project Set Up and Installation
Upload the pima_diabetes.csv file in the Dat section of AzureML as a tabular file. Name of the data asset should be pima-diabetes
The AutoML run can be run by just running the automl.ipynb notebook
The conda_dependencies.yml file should be present in Azure file system when running the hyperdrive run run in the hyperparameter_tuning.ipynb notebook


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
experiment_timeout_minutes=30, maximum time upto which the AutoML run will continue. Helps in reducing unneccessary use of cluster time

task='classification', the task is to clasify whether a person has diabetes or not

primary_metric='accuracy', The metric being tracked is Accuracy

training_data=train_ds, train_ds is the training dataset

label_column_name='Outcome', 'Outcome' is the column in the dataset whihc is the target column to be predicted

n_cross_validations=5, number of cross validations ot perform to get the metric

compute_target = cpu_cluster, the compute cluster whihc has been created in the code

### Results
The AutoML model provided a best accuracy of around 0.78. The Voting Ensemble model which was a ensemble of different models like Logistic regression, XGBoostClassifier, RandomForestClassifier etc. There wany different models of a single type inthe ensemble with different hyperparameters. each model had a weight assigned to it and a scaling technique for preprocessing the data. More details about the model can be obtained in the automl.ipynb notebook

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/a99c10e7-a50d-4b25-b7d3-57f11adeeca4)
Logistic regression was the best performing model in terms of accuracy. The XGBoost classifier models were second. Thereafter, other models like LIghtGBM, RandomForestClassifier, ExtremeRandomTrees followed in terms of accuracy

AutoML training and Best Model
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/1fd419df-1227-486e-befa-ddc7f02c8bed)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/0d4b6521-2964-46c5-a278-73f3bcfd0857)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/8e66a78c-350c-421f-935c-5b3636c55120)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/3d8c663a-1739-46fc-963e-44a0bd036ebf)


![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/7f7e84c4-8fe0-41d2-8b5a-8817b90231a9)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/dc098a05-3760-4f86-90a9-b05b5d5afedc)

Best model metrics
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/5f575cd7-096d-4312-a378-1bbf14b92c81)


Deployed model screenshot from AzureML UI
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/ff89103e-4eed-4cc6-b8d2-9fcbfab2bcc1)

Call to the deployed model endpoint using endpoint.py and returned result from model
![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/84ec562a-cb11-4da9-8fd8-d148091a9ace)



## Hyperparameter Tuning

Logistic regression model was chosen because of this being a binary classfication task. The hyperparameters being optimized were inverse regularization strength 'C' and number of iterations 'iter'. The C paramters was varied in the range 0.1 to 0.4 and the number of iteratins were chosen randomly from 12,25 and 50


### Results

The max accuracy was around 0.75. The parameters were C=0.349 and iter=50. regularization strength reduces the overfitting tendency and number of iterations gives time to the gradient descent optimization in hte logistics regression loss function minimization. Thesea re the reasons behind choosing these 2 hyperparameters.

Increasing the number of iterations could increase the model performance because it can be seen in th escreenshots that the highest accuracy was observed of iterations=50. The effect of C on accuracy is not very evident from the results bu the range of C can be increased nevertheelsess from 0 to 1 to check performance. Also,  techniques like Bayesian parameter sampling which take into account the previous explored hyperparameters to reduce wasteful search can improve the hyperparameter optimization. 


![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/a0198ba6-81bb-4b4d-9993-9f54986981b5)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/4cd5290b-2254-4a96-94ea-53a3a6f4d97b)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/874a8966-be3a-4a5b-ae64-54807f0788ba)

![image](https://github.com/soumyadiptapete/Captstone-AzureML-MLEngineer-Nanodegree/assets/20270621/7a870b5f-d357-4daa-acf9-0f52b2299560)

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
[https://youtu.be/-eC-X_bmFOs](https://youtu.be/KYXcdR8ppfM)

## Project Improvements
Exploratory data analysis to check for features which are having some correlations with the predicted variable using chi square tests will help in choosing important features. Increasing the timeout of AutoML might help in exploring a wider range of models.
For Hyperdriv, increasing the number of iterations could increase the model performance because it can be seen in th escreenshots that the highest accuracy was observed of iterations=50. The effect of C on accuracy is not very evident from the results bu the range of C can be increased nevertheelsess from 0 to 1 to check performance. Also,  techniques like Bayesian parameter sampling which take into account the previous explored hyperparameters to reduce wasteful search can improve the hyperparameter optimization. 
## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
