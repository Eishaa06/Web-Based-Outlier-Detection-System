# Import joblib
import joblib
import os  # Add import for os module


# Import necessary libraries
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Step 1: Data loading
data = pd.read_csv(r"C:\Users\Esha\Desktop\detect\creditcard.csv")


# Step 2: Data Preprocessing
# Remove duplicates
data.drop_duplicates(inplace=True)

# Remove missing values
data.dropna(inplace=True)

# Add labels to the data
data["Label"] = 1
data.loc[data["Class"] == 1, "Label"] = -1

# Step 3: Algorithm Selection
# Select Isolation Forest algorithm for outlier detection
model = IsolationForest(contamination=0.01)

# Step 4: Algorithm Implementation
# Split data into training and testing sets
train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

# Train the model on the training set
model.fit(train_data.drop(columns=["Class", "Label"]))

# Evaluate the model's performance on the testing set
predictions = model.predict(test_data.drop(columns=["Class", "Label"]))
print(classification_report(test_data["Label"], predictions))

# Step 5: Outlier Detection
# Apply the trained model to the full dataset to identify and label outliers
data["Outlier"] = model.predict(data.drop(columns=["Class", "Label"]))

# Step 6: Report Generation
# Generate a report summarizing the results of the analysis
outliers = data[data["Outlier"] == -1]
print(f"Number of outliers detected: {len(outliers)}")

# Check the current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# After training, save the model using joblib
model_filename = 'isolation_forest_model.joblib'



# Load the model using joblib
model_path = os.path.join(current_dir, model_filename)
loaded_model = joblib.load(model_path)

# Evaluate the model's performance on the testing set
predictions = loaded_model.predict(test_data.drop(columns=["Class", "Label"]))
print(classification_report(test_data["Label"], predictions))

# Step 5: Outlier Detection
# Apply the trained model to the full dataset to identify and label outliers
data["Outlier"] = loaded_model.predict(data.drop(columns=["Class", "Label"]))