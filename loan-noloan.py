import streamlit as st
import pandas as pd
import numpy as np
import joblib
from xgboost import XGBClassifier

st.set_option('deprecation.showfileUploaderEncoding', False)
st.write("""
# Loan or No Loan?
""")
st.write('---')

def user_input_features():
    loanid = st.text_input('ENTER LOANID')
    income = st.number_input('ENTER APPLICANT\'S INCOME')
    coincome = st.number_input('ENTER CO-APPLICANT\'S INCOME')
    loanamt= st.number_input('ENTER LOAN AMOUNT')
    amtterm = st.number_input('ENTER LOAN AMOUNT TERM')
    if st.checkbox('Married'):
        m_no = 0
        m_yes = 1
    else:
        m_no = 1
        m_yes = 0
    dependent =  st.number_input('ENTER NUMBER OF DEPENDENTS')
    if(dependent>=3):
        dependent = 4
    if st.checkbox('SELF-EMPLOYED'):
        se_no = 0
        se_yes = 1
    else:
        se_no = 1
        se_yes = 0
    if st.checkbox('GRADUATE'):
        g_no = 0
        g_yes = 1
    else:
        g_no = 1
        g_yes = 0
    region = st.selectbox('SELECT PROPERTY AREA', ['Rural', 'Semiurban', 'Urban'])
    if(region == 'Rural'):
        rural = 1
        urban = 0
        surban = 0
    elif(region == 'Urban'):
        rural = 0
        urban = 1
        surban = 0
    else:
        rural = 0
        urban = 0
        surban = 1

    input_data = {'Dependents': dependent,
            'ApplicantIncome': income,
            'CoapplicantIncome': coincome,
            'LoanAmount': loanamt,
            'Loan_Amount_Term': amtterm,
            'Married_No': m_no,
            'Married_Yes': m_yes,
            'Self_Employed_No': se_no,
            'Self_Employed_Yes': se_yes,
            'Education_Graduate': g_yes,
            'Education_Not Graduate': g_no,
            'Property_Area_Rural': rural,
            'Property_Area_Semiurban': surban,
            'Property_Area_Urban': urban}
    features = pd.DataFrame(input_data, index=[0])
    return features

input_df = user_input_features()

load_clf = joblib.load('loan.pkl')

if st.button("Predict"):
    output = load_clf.predict(input_df)
    if(output == 1):
        out = 'LOAN APPLICATION APPROVED'
    else:
        out = 'LOAN APPLICATION REJECTED'
st.success(out)

st.write('---')