import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://c14d2cfc-7fe2-42f9-94f4-a03f344bfb75.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = '4cDLSwDUtU79cJTkpgOyVXXfLuR3nvhc'

# Two sets of data to score, so we get two results back
data = {
    'data': [
        {'Pregnancies': 6, 'Glucose': 8, 'BloodPressure':72, 'SkinThickness':35, 'Insulin':0,
    'BMI':33.6,'DiabetesPedigreeFunction':0.627,'Age':50}  
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


