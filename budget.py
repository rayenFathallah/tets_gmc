import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("budget calculation")


income=st.number_input("## Input your income")

expenses=["Renting","Groceries", "Entertainment", "Miscellaneous"]
Expenses=[]

for exp in expenses:
   ex=st.number_input(f"Give expenses of:{exp}")
   if ex:
    Expenses.append(ex)
   else:
    Expenses.append(0)  

percent=st.slider("## Select your saving goal (percentage):",0,100,step=5)

if st.button("Calculate your budget"):

    st.info(f" Total of expenses = {sum(Expenses)}")

    

    saving=income-sum(Expenses)

    st.info(f"target saving : {percent}%")

    if saving > (income * (percent/100)):
        st.success("Congratulation You are saving well")
    else:
        st.warning("Try to cut down on expenses!")

    st.info(f" The category has the maximum expense: {expenses[Expenses.index(max(Expenses))]}")

    x=np.array(expenses)
    y=np.array(Expenses)
    plt.bar(x,y)
    plt.title("Expenses")
    plt.xlabel("Expenses")
    plt.ylabel("values")   
    st.pyplot(plt)



