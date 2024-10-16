import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simple Personal Budget Calculator")
st.text_input("name")
st.radio("Marital status",["Engaged", "Single", "Other"])
monthly_income=st.number_input("Monthy income")
rent=st.number_input("Rent")
utilities=st.number_input("Utilities")
groceries=st.number_input("Groceries")
entertainment=st.number_input("Entertainment")
miscellaneous=st.number_input("Miscellaneous")
total_expences=entertainment+miscellaneous+groceries+utilities+rent
st.write(f"Total expences = {total_expences}")
monthly_saves=monthly_income-total_expences
st.write(f"Monthly saves = {monthly_saves}")
saving_goal=st.slider("Saving goal %",0, 100, 10)
st.write(f"{saving_goal*monthly_income/100}")
if (saving_goal*monthly_income/100<monthly_saves):
    st.write("You are saving well!")
else:
    st.write("Try to cut down on expenses!")

dict={"Rent":rent,"utilities":utilities, "groceries":groceries,
           "entertainment":entertainment,"miscellaneous":miscellaneous}
max=0
max_category=''
for elt in dict.items():
    key,value=elt
    if value>max:
        max=value
        max_category=key

st.write(f"{max_category}")

plt.bar(dict.keys(), dict.values())
plt.title="Expences"
plt.xlabel="fndsfl"
st.pyplot(plt)

    