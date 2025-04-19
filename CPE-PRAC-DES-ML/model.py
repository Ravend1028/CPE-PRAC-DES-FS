import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
import joblib

# Dataset URL
sheet_id = "1WlahHdcxQBPiSDCxJNZ1BeXLzZki2Xdv"
sheet_name = "FINAL_DS"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Load Dataset
df = pd.read_csv(url)

# Data Separation
y = df[['Underweight', 'Overweight', 'Obesity', 'Hypertension', 'Hypotension' ,'Hypoxia', 'Fever', 'Hypothermia' ,'Bradycardia', 'Tachycardia', 'Respiratory Distress']]
X = df.drop(['Underweight', 'Overweight', 'Obesity', 'Hypertension', 'Hypotension' ,'Hypoxia', 'Fever', 'Hypothermia' ,'Bradycardia', 'Tachycardia', 'Respiratory Distress'], axis=1)

# Data Splitting 80-20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Model Building / Params Config
rf = RandomForestClassifier(max_depth=2, n_estimators=200, max_features=7, random_state=100)
multi_target_model = MultiOutputClassifier(rf)

# Model Training
multi_target_model.fit(X_train, y_train)

# Save the train model
joblib.dump(multi_target_model, 'model.joblib')
