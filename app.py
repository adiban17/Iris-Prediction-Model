# importing required libraries
import streamlit as st
import joblib

# giving the interface a title and a description
st.title("Iris Flower Species Classification Using Machine Learning")
st.write("This machine learning model predicts the species of iris flowers—setosa, versicolor, or virginica—based on their sepal and petal dimensions. By utilizing a dataset containing measurements of sepal length, sepal width, petal length, and petal width, the model employs classification algorithms to analyze the relationships between these features. The trained model can accurately classify new iris flower samples, aiding in botanical research and species identification. This application demonstrates the power of machine learning in solving real-world classification problems in biology.")

# taking the required inputs from the user
sepal_length=st.slider("Sepal Length (in cm)", min_value=4.3, max_value=7.9)
sepal_width=st.slider("Sepal Width (in cm)", min_value=2.0, max_value=4.4)
petal_length=st.slider("Petal Length (in cm)", min_value=1.0, max_value=6.9)
petal_width=st.slider("Petal Width (in cm)", min_value=0.1, max_value=2.5)

# loading the ML model
model=joblib.load('iris_prediction_model.pkl')
species=model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

# making predictions and displaying it to the user
if species==1:
    st.header("Iris Species: Iris-setosa")
elif species==2:
    st.header("Iris Species: Iris-virginica")
else:
    st.header("Iris Species: Iris-versicolor")

