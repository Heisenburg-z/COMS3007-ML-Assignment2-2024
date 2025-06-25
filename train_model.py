import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from joblib import dump

# Load training data
train_data = pd.read_csv("traindata.txt", header=None)
train_labels = pd.read_csv("trainlabels.txt", header=None).values.ravel()

# Define the pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Define the parameter grid for hyperparameter tuning
param_grid = {
    'classifier__n_estimators': [100, 200, 300],
    'classifier__max_depth': [10, 20, 30],
    'classifier__min_samples_split': [2, 5, 10]
}

# Perform grid search with cross-validation
grid_search = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(train_data, train_labels)

# Train the best model
best_model = grid_search.best_estimator_

# Save the trained model to a file
dump(best_model, 'trained_model.joblib')
print("Best Model Parameters:", grid_search.best_params_)

