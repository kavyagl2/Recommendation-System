import streamlit as st
import pickle
import pandas as pd
from fuzzy_logic import recommend_teaching_and_learning_style

# Load the advanced clustering model and feature columns
with open("models/advanced_clustering_model.pkl", "rb") as f:
    clustering_model = pickle.load(f)

with open("models/feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

# Streamlit App Layout
st.title("Advanced Teaching & Learning Style Recommendation System")

st.subheader("Input Information")

# User Input Fields
subject = st.selectbox("Select Subject", [
    "Thermodynamics", "Fluid Mechanics", "Heat Transfer", "Manufacturing Processes",
    "Machine Design", "Mechanics of Materials", "CAD", "Control Systems",
    "Mechatronics", "Engineering Mechanics"
])
characteristics = st.selectbox("Select Characteristics", ["Design-oriented", "Analytical", "Experimental"])
lab_subject = st.selectbox("Is it a lab subject?", ["Yes", "No"])
subject_type = st.selectbox("Type of Subject", ["Core", "Elective"])

# Duration input with manual entry (integer or decimal)
duration = st.text_input("Enter Duration (hours)", value="10.0")

# Validate duration input
try:
    duration = float(duration)
except ValueError:
    st.error("Please enter a valid number for Duration.")
    st.stop()

requirements = st.selectbox("Primary Requirement", ["Theoretical", "Lab"])
learning_background = st.selectbox("Learning Background", ["UG", "PG"])
teacher_experience = st.selectbox("Teacher Experience Level", ["New", "Intermediate", "Experienced"])
lab_facility = st.selectbox("Lab Facility Availability", ["Available", "Not Available"])

# Convert inputs for clustering
learning_ability_numeric = 1 if teacher_experience == "Experienced" else 0.5 if teacher_experience == "Intermediate" else 0
lab_facility_numeric = 1 if lab_facility == "Available" else 0

# Collect all input data into a DataFrame
input_df = pd.DataFrame({
    "Duration": [duration],
    "Learning Ability": [learning_ability_numeric],
    "Lab Facility": [lab_facility]
})

# One-hot encode user input using the training structure
input_encoded = pd.get_dummies(input_df, drop_first=True)

# Align the input features to match the training columns (add missing columns with 0)
input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

# Button to trigger recommendation
if st.button("Request Recommendations"):
    # Use DataFrame with feature names directly to avoid the warning
    try:
        cluster = clustering_model.predict(input_encoded)[0]
    except ValueError as e:
        st.error(f"Error in input features: {e}")
        st.stop()

    # Generate recommendation (teaching and learning styles)
    recommended_styles = recommend_teaching_and_learning_style(cluster, learning_ability_numeric)
    teaching_style = recommended_styles['teaching_style']
    learning_style = recommended_styles['learning_style']
    confidence = recommended_styles['confidence']

    # Display Recommendations in a Tabular Format
    st.subheader("Recommendations")
    # Format data into a DataFrame for a cleaner table display
    recommendation_df = pd.DataFrame({
        "Recommended Teaching Styles": teaching_style,
        "Recommended Learning Styles": learning_style,
        "Confidence Level (%)": [f"{confidence * 100:.2f}"] * len(teaching_style)
    })
    
    # Display the DataFrame as a table
    st.table(recommendation_df)
