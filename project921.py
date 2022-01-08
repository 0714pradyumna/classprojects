import streamlit as st

def calculate_emi(p,n,r) :
  emi = p * (r / 100) * (((1 + (r/100))** n) / (((1 + r/100) ** n) - 1))
  return round(emi, 3)

st.title("EMI Calculator App")  

principal = st.slider('Principal', 10000, 50000)
tenure = st.slider('Tenure', 1, 30)
roi = st.slider('Rate of interest', 1.00, 15.00)

n = tenure * 12
r = roi / 12

if st.button('Calculate') :
  calculated_emi = calculate_emi(principal, n, r)
  st.write('If the Principal Amount borrowed is ', principal, 'for the tenure of ', n, 'months with Rate of interest as ', r, 'percent per annum then the Emi will be ', calculated_emi)
