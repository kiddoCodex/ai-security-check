# predict_security.py
import sys
import pickle

# Load the pre-trained machine learning model
with open('system_security_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Get the features passed from Bash
features = list(map(int, sys.argv[1].split(',')))

# Predict the security status (1: secure, 0: at risk)
prediction = model.predict([features])

# Print the prediction (1 or 0)
print(prediction[0])