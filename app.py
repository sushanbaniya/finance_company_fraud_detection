import streamlit as st
import joblib 
import numpy as np

fraud_model = joblib.load('fraudmodel.pkl')

st.title('INTERNSHIP TASK: Predicting fraudlent transaction for finance company')

st.divider()

step = st.number_input('Enter step of transaction', min_value=1, max_value=743, value=725)

amount = st.number_input('Enter amount of transaction', min_value=0, max_value=17112030, value=10000000)

oldbalanceOrg = st.number_input('Enter old balance of customer who started transaction', min_value=0 , max_value= 59585040, value=50000000)

newbalanceOrig = st.number_input('Enter new balance of customer who started trandaction', min_value=0 , max_value=49585040 , value=40000000)

oldbalanceDest = st.number_input('Enter old balance of recepient', min_value= 0, max_value=236230500 , value=200000000)

newbalanceDest = st.number_input('Enter new balance of recepient', min_value=0 , max_value=236726500 , value=200000000)

isFlaggedFraud = st.number_input('Enter if it is flagged fraud or not', min_value=0, max_value=1, value=1)

st.divider()

X = [[step,amount,oldbalanceOrg,newbalanceOrig,oldbalanceDest,newbalanceDest,isFlaggedFraud]]

X_array = np.asarray(X)

btn = st.button('Predict')

if btn:
    prediction = fraud_model.predict(X_array)
    st.write('On the basis of above input, the value of \'isFraud\' variable is: ', prediction[0])
    if(prediction[0] == 0):
        st.write(':green[So, The Transaction is LEGIT(NOT FRAUD) !]')
    elif(prediction[0] ==1):
        st.write(':red[So, The Transaction is FRAUD !]')
    print(prediction)

st.divider()

st.write('Developed by SUSHAN BANIYA')


