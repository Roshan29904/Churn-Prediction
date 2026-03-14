import streamlit as st
import pandas as pd
import pickle

#Load the model 
with open("model.pkl","rb") as f:
    model = pickle.load(f)


#create the app

st.title("Predict Customer Churn")

#getting inputs from the user

gender=st.selectbox("Gender",["Male","Female"],index=None,placeholder="select gender")
senior_citizen=st.selectbox("senior citizen",["Yes","No"],index=None,placeholder="select senior citizen")
partner=st.selectbox("Partner",["Yes","No"],index=None,placeholder="select partner")
dependents=st.selectbox("Dependents",["Yes","No"],index=None,placeholder="select dependents")
tenure=st.number_input("Tenure",min_value=0,value=None,placeholder="enter tenure")
phone_service=st.selectbox("Phone service",["Yes","No"],index=None,placeholder="select phone service")
multiple_lines=st.selectbox("Multiple lines",["Yes","No",'No phone service'],index=None,placeholder="select multiple lines")
internet_service=st.selectbox("Internet service",["DSL","Fiber optic","No"],index=None,placeholder="select internet service")
online_security=st.selectbox("Online security",["Yes","No",'No internet service'],index=None,placeholder="select online security")
online_backup=st.selectbox("Online backup",["Yes","No",'No internet service'],index=None,placeholder="select online backup")
device_protection=st.selectbox("Device protection",["Yes","No",'No internet service'],index=None,placeholder="select device protection")
tech_support=st.selectbox("Tech support",["Yes","No",'No internet service'],index=None,placeholder="select tech support")
streaming_tv=st.selectbox("streaming tv",["Yes","No",'No internet service'],index=None,placeholder="select streaming tv")
streaming_movies=st.selectbox("streaming movies",['No', 'Yes', 'No internet service'],index=None,placeholder="select streaming movies")
contact=st.selectbox("Contact",['One year', 'Two year', 'Month-to-month'],index=None,placeholder="select contact")
paperless_billing=st.selectbox("Paperless billing",["Yes","No"],index=None,placeholder="select paperless billing")
payment_method=st.selectbox("payment method",['Mailed check','Credit card (automatic)','Electronic check', 'Bank transfer (automatic)'],index=None,placeholder="select payment method")
monthly_charges=st.number_input("Monthly charges",min_value=0.0,value=None,placeholder="enter monthly charges")
total_charges=st.number_input("Total charges",min_value=0.0,value=None,placeholder="enter total charges")


#setting default values for the inputs i.e NaN values



if st.button("Predict"):
    input_dict = {
        'gender': gender,
        'SeniorCitizen': senior_citizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contact,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges
    }
    df = pd.DataFrame([input_dict])
   
    churn = model.predict_proba(df)[0][1]
    
    #if all the inputs are not provided
    if  not all([gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contact, paperless_billing, payment_method, monthly_charges, total_charges]):
        st.warning("Please provide all the inputs to get a prediction.")
    
    elif churn >= 0.5:
        st.error("The customer is likely to churn.")
    else:
        st.success("The customer is not likely to churn.")
     
    
