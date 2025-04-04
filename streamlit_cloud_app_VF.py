import joblib
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt
import mlflow
import numpy as np
import pandas as pd
import shap
import streamlit as st

# Set the MLflow tracking URI
# mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

# IMPORTANT : in advanced settings, choose python 3.10 when deploying app in streamlit cloud
# to avoid error on loading distutils which is discontinued from python 3.12 onwards

def main():

    def convert_dtypes(df):
        """Convert dataframe columns to appropriate types."""
        for col in df.columns:
            if df[col].dtype == "object":
                try:
                    df[col] = pd.to_numeric(df[col])
                except ValueError:
                    pass  # Keep as string if conversion fails
        return df

    def load_model(model_name):
        """Load the MLflow model with its preprocessing pipeline."""
        try:
            # return mlflow.pyfunc.load_model(model_uri)
            return joblib.load(model_name)
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None

    def get_model_predictions(model, input_df, threshold=0.502):
        """Get predictions from the model, including preprocessing."""
        try:
            input_df = convert_dtypes(input_df)
            probabilities = model.predict(input_df)
            probabilities = np.array(probabilities).astype(float)
            predictions = np.where(probabilities > threshold, 1, 0)
            actions = np.where(probabilities > threshold, "Reject application", "Grant loan")
            return probabilities, predictions, actions
        except Exception as e:
            st.error(f"Error in prediction: {str(e)}")
            return None, None, None

    # def generate_shap_values():
    # Streamlit SHAP can't handle pipelines & preprocessor objects
    # Load data pre-processed externally
    # X_train = pd.read_csv('X_resampled.csv')
    # X_train = convert_dtypes(X_train)
    # y_train = pd.read_csv('y_resampled.csv')
    # y_train = convert_dtypes(y_train)
    # X_test = pd.read_csv('X_test_preprocessed.csv')
    # X_test = convert_dtypes(X_test)
    # try:
    # Load params from best model - cannot use MLFlow logged model here either
    # as it was logged with pre-processing pipeline which Shap can't handle
    # final_params_lgbm = {'is_unbalance': True,
    #  'learning_rate': 0.1,
    #  'max_depth': 6,
    #  'min_data_in_leaf': 400,
    #  'min_gain_to_split': 0.001,
    #  'num_leaves': 60,
    #  'random_state': 42}

    # Instanciate model
    # best_lgbm_classif= LGBMClassifier(**final_params_lgbm, verbose=-1)

    # Fit model
    # best_lgbm_classif = best_lgbm_classif.fit(X_train, y_train)

    # Create the SHAP explainer using the model's predict method
    # explainer = shap.TreeExplainer(best_lgbm_classif)

    # Calculate SHAP values for input data
    # shap_values = explainer.shap_values(X_test)

    # return shap_values, explainer, X_test

    # except Exception as e:
    # st.error(f"Error generating SHAP values: {str(e)}")
    # return None

    # Streamlit UI
    st.title("Welcome to the ")
    st.image("logo.png")
    st.title("Credit Scoring App ! ")
    st.write("Upload a CSV file to analyse your client's application file:")

    # File uploader for CSV input
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read and preprocess input data
        input_data = pd.read_csv(uploaded_file)
        index = input_data["row_number"].values[0]
        input_data = input_data.drop(labels="row_number", axis=1)
        input_data = convert_dtypes(input_data)
        st.write("Data loaded.")
        # st.write(input_data)

        # st.write("Column Types:")
        # st.write(input_data.dtypes)

        # Load the model (which includes the preprocessing pipeline)
        # model_uri = 'runs:/55c3ad49505d42f8b6d08af08975159b/final_scoring_model'
        model_name = "final_model.joblib"
        # model = load_model(model_uri)
        model = load_model(model_name)

        if model is not None:
            # Get predictions (model.predict includes preprocessing)
            probabilities, predictions, actions = get_model_predictions(model, input_data)

            st.write(f"Client number: {index}")

            if probabilities is not None:
                st.write("Predicted Probabilities:")
                st.write(probabilities[0, 1])

                st.write("Predictions (Binary):")
                st.write(predictions[0, 1])

                st.title("Actions:")
                st.write(actions[0, 1])

                # Generate SHAP values (using model's preprocessing)
                # shap_values, explainer, X_test = generate_shap_values()
                # st.write(X_test.shape)
                # st.write(len(shap_values[index]))
                # st.write(explainer.expected_value)
                # st.write(X_test.loc[index].shape)
                # st.write(len(X_test.columns))
                # st.write(X_test.loc[index])
                # st.write()

                # if shap_values is not None:
                # Create SHAP waterfall plot for the first prediction
                # fig, ax = plt.subplots(figsize=(10,6))
                # st.title(f"Key decision factors for client {index} :")
                # shap.plots.waterfall(shap.Explanation(values=shap_values[index],
                # base_values=explainer.expected_value,
                # data=X_test.loc[index],
                # feature_names=X_test.columns),
                # show=True,
                # max_display=6)
                # st.pyplot(fig)

    # st.write("Note: This app uses a pre-trained model with its associated preprocessing pipeline.")


if __name__ == "__main__":
    main()
