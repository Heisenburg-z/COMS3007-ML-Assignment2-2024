import numpy as np
import pandas as pd
from joblib import load

def main():
    # Load test data
    test_data = pd.read_csv("testdata.txt", header=None)

    # Load the pre-trained model
    model = load('trained_model.joblib')

    # Predict labels for test data
    pred_labels = model.predict(test_data)

    # Save predictions to 'predlabels.txt'
    pred_labels_df = pd.DataFrame(pred_labels)
    pred_labels_df.to_csv("predlabels.txt", index=False, header=False)

if __name__ == "__main__":
    main()

