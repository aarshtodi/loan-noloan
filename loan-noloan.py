import streamlit as st
import pandas as pd
import numpy as np
import joblib
from xgboost import XGBClassifier

load_clf = joblib.load('loan.pkl')

def run():

    st.sidebar.info('A loan application is used by borrowers to apply for a loan. Through the loan application, borrowers reveal key details about their finances to the lender. The loan application is crucial to determining whether the lender will grant the request for funds or credit.This app automates the entire process.')
    st.sidebar.write('---')

    st.title("Loan or No Loan?")
    st.write('---')

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

    input_dict = {'Dependents': dependent,
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
    input_df = pd.DataFrame([input_dict])

    if st.button("Predict"):
        output = load_clf.predict(input_df)
        if(output == 1):
            out = "APPROVED"
        else:
            out = "REJECTED"
        st.success(out)

if __name__ == '__main__':
    run()