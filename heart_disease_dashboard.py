import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data_path = 'heart_disease.csv'  # Update with the path to your file if different
df = pd.read_csv(data_path)
# Title of the dashboard
st.title("Heart Disease Analysis Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
age_filter = st.sidebar.slider("Age Range", int(df.Age.min()), int(df.Age.max()), (40, 60))
df_filtered = df[(df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1])]

# Plot 1: Age Distribution by Heart Disease
st.subheader("Age Distribution by Heart Disease")
fig_age = px.histogram(df_filtered, x="Age", color="HeartDisease", marginal="box",
                       title="Age Distribution with Heart Disease Outcome", 
                       labels={"HeartDisease": "Heart Disease", "Age": "Age"})
st.plotly_chart(fig_age)

# Plot 2: Cholesterol Distribution by Heart Disease
st.subheader("Cholesterol Distribution by Heart Disease")
fig_cholesterol = px.histogram(df_filtered, x="Cholesterol", color="HeartDisease", marginal="box",
                               title="Cholesterol Distribution by Heart Disease Outcome", 
                               labels={"HeartDisease": "Heart Disease", "Cholesterol": "Cholesterol"})
st.plotly_chart(fig_cholesterol)

# Plot 3: Resting Blood Pressure by Heart Disease
st.subheader("Resting Blood Pressure by Heart Disease")
fig_bp = px.histogram(df_filtered, x="RestingBP", color="HeartDisease", marginal="box",
                      title="Resting Blood Pressure by Heart Disease Outcome", 
                      labels={"HeartDisease": "Heart Disease", "RestingBP": "Resting BP"})
st.plotly_chart(fig_bp)

# Plot 4: MaxHR vs Age colored by Heart Disease
st.subheader("MaxHR vs Age by Heart Disease")
fig_hr_age = px.scatter(df_filtered, x="Age", y="MaxHR", color="HeartDisease",
                        title="MaxHR vs Age by Heart Disease",
                        labels={"HeartDisease": "Heart Disease", "MaxHR": "Max Heart Rate", "Age": "Age"})
st.plotly_chart(fig_hr_age)

# Plot 5: Cholesterol by Chest Pain Type
st.subheader("Cholesterol Levels by Chest Pain Type and Heart Disease")
fig_chest_cholesterol = px.box(df_filtered, x="ChestPainType", y="Cholesterol", color="HeartDisease",
                               title="Cholesterol Levels by Chest Pain Type",
                               labels={"ChestPainType": "Chest Pain Type", "Cholesterol": "Cholesterol", "HeartDisease": "Heart Disease"})
st.plotly_chart(fig_chest_cholesterol)

# Plot 6: Count of Chest Pain Type by Heart Disease
st.subheader("Count of Chest Pain Type by Heart Disease")
fig_chest_pain = px.histogram(df_filtered, x="ChestPainType", color="HeartDisease", barmode="group",
                              title="Chest Pain Type by Heart Disease",
                              labels={"ChestPainType": "Chest Pain Type", "HeartDisease": "Heart Disease"})
st.plotly_chart(fig_chest_pain)

# Plot 7: Oldpeak by ST_Slope
st.subheader("Oldpeak Levels by ST Slope and Heart Disease")
fig_oldpeak = px.scatter(df_filtered, x="Oldpeak", y="Age", color="ST_Slope", symbol="HeartDisease",
                         title="Oldpeak Levels by ST Slope",
                         labels={"Oldpeak": "Oldpeak", "ST_Slope": "ST Slope", "HeartDisease": "Heart Disease"})
st.plotly_chart(fig_oldpeak)

# Footer note
st.markdown("Dashboard created using **Plotly** and **Streamlit**.")
