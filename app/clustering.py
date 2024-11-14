import pandas as pd
from sklearn.mixture import GaussianMixture
import pickle

def train_advanced_clustering_model():
    # Load the synthetic dataset
    df = pd.read_csv("data/synthetic_teaching_data.csv")

    # Select relevant features for clustering
    features = df[["Duration", "Learning Ability", "Lab Facility"]]
    
    # One-hot encode categorical features and save the encoder structure
    features_encoded = pd.get_dummies(features, drop_first=True)
    
    # Save the columns used for one-hot encoding for future predictions
    with open("models/feature_columns.pkl", "wb") as f:
        pickle.dump(features_encoded.columns, f)

    # Use Gaussian Mixture Model for clustering
    gmm = GaussianMixture(n_components=6, random_state=42)
    df["Cluster"] = gmm.fit_predict(features_encoded)

    # Save the model
    with open("models/advanced_clustering_model.pkl", "wb") as f:
        pickle.dump(gmm, f)

    print("Advanced clustering model trained and saved to models/advanced_clustering_model.pkl")

# Run clustering model training
if __name__ == "__main__":
    train_advanced_clustering_model()
