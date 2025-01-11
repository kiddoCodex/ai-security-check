# ml_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Sample system audit data
# Each row represents a system configuration with features and labels (secure or at risk)
data = {
    'ssh_root_login': [1, 0, 1, 0, 0, 1, 0],  # 1: enabled, 0: disabled
    'firewall_active': [1, 1, 0, 1, 0, 1, 1],  # 1: active, 0: inactive
    'permissions_secure': [1, 0, 1, 1, 0, 0, 1],  # 1: secure, 0: insecure
    'system_up_to_date': [1, 1, 0, 1, 1, 0, 1],  # 1: up-to-date, 0: outdated
    'disk_usage_safe': [1, 1, 1, 1, 0, 1, 1],  # 1: safe, 0: high usage
    'secure': [1, 0, 1, 1, 0, 0, 1]  # 1: secure, 0: at risk (target variable)
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Features (input data)
X = df.drop(columns=['secure'])

# Target variable (output label)
y = df['secure']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Save the model for later use
with open('system_security_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)