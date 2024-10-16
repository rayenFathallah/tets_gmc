import streamlit as st
st.title('Budget')
st.subheader("Personal details")
user_name = st.text_input("Enter your name:")
marital_status = st.radio("Select your marital status:",
    options=["Single", "Married", "Divorced", "Widowed"])
st.text(f"the marital status is {marital_status} ")
st.subheader("Financial situation")
monthly_income = st.number_input("Enter your monthly income:", min_value=0.0, step=50.0)
rent = st.number_input("Enter your Rent:", min_value=0.0, step=10.0)
utilities = st.number_input("Enter your Utilities:", min_value=0.0, step=10.0)
groceries = st.number_input("Enter your Groceries:", min_value=0.0, step=10.0)
entertainment = st.number_input("Enter your Entertainment:", min_value=0.0, step=10.0)
miscellaneous = st.number_input("Enter your Miscellaneous expenses:", min_value=0.0, step=10.0)
total_expenses = rent+utilities+groceries+entertainment+miscellaneous
if st.button("Next"):
    st.success("Next values")
    monthly_savings = monthly_income - total_expenses
    st.write(f"**Monthly Savings:** ${monthly_savings:,.2f}")
    savings_goal_percentage = st.slider("Set your savings goal (% of income):", min_value=0, max_value=100, value=20)
    savings_goal = (savings_goal_percentage / 100) * monthly_income
    if monthly_savings >= savings_goal:
       st.success("You are saving well!")
    else:
       st.warning("Try to cut down on expenses")
    expense_categories = {
        "Rent": rent,
        "Utilities": utilities,
        "Groceries": groceries,
        "Entertainment": entertainment,
        "Miscellaneous": miscellaneous
    }
    highest_expense_category = max(expense_categories, key=expense_categories.get)
    highest_expense_amount = expense_categories[highest_expense_category]
    import pandas as pd
    st.write(f"### Highest Expense Category: {highest_expense_category} (${highest_expense_amount:,.2f})")
    df_expenses = pd.DataFrame(expense_categories.items(), columns=["Category", "Amount"])
    st.write("### Expenses by Category")
    st.bar_chart(df_expenses.set_index("Category"))