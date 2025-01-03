import streamlit as st
from prediction_helper import predict

# Set up the title and header
st.title("Credit Risk Modeling")
st.markdown("### Evaluate loan applicants and assess their credit risk effectively.")

# Organize inputs into collapsible sections
with st.expander("Personal Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=18, max_value=100, step=1)
    with col2:
        income = st.number_input('Annual Income (₹)', min_value=0, max_value=1200000, step=10000)
    with col3:
        residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])

with st.expander("Loan Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        loan_amount = st.number_input('Loan Amount (₹)', min_value=0, max_value=2560000, step=10000)
    with col2:
        loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=6, max_value=360, step=6, value=36)
    with col3:
        loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])

    col1, col2 = st.columns(2)
    with col1:
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])
    with col2:
        loan_to_income_ratio = loan_amount / income if income > 0 else 0
        st.metric("Loan-to-Income Ratio", f"{loan_to_income_ratio:.2f}")

with st.expander("Credit History", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        num_open_accounts = st.number_input('Number of Open Loan Accounts', min_value=1, max_value=10, step=1, value=2)
    with col2:
        delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30)
    with col3:
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30)

    col1, col2 = st.columns(2)
    with col1:
        avg_dpd_per_delinquency = st.number_input('Average DPD per Delinquency', min_value=0, value=20)
    with col2:
        st.text("")

# Add a submit button
if st.button('Calculate Risk'):
    # Input Summary Section
    st.success("Risk calculation initiated!")
    st.write("### Input Summary")
    st.write(f"**Age:** {age} years")
    st.write(f"**Income:** ₹{income:,}")
    st.write(f"**Loan Amount:** ₹{loan_amount:,}")
    st.write(f"**Loan-to-Income Ratio:** {loan_to_income_ratio:.2f}")
    st.write(f"**Loan Tenure:** {loan_tenure_months} months")
    st.write(f"**Average DPD per Delinquency:** {avg_dpd_per_delinquency}")
    st.write(f"**Delinquency Ratio:** {delinquency_ratio}%")
    st.write(f"**Credit Utilization Ratio:** {credit_utilization_ratio}%")
    st.write(f"**Number of Open Accounts:** {num_open_accounts}")
    st.write(f"**Residence Type:** {residence_type}")
    st.write(f"**Loan Purpose:** {loan_purpose}")
    st.write(f"**Loan Type:** {loan_type}")

    # Predict Output
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)

    # Output Details Section
    st.write("### Output Details")
    st.write(f"**Default Probability:** {probability:.2%}")
    st.write(f"**Credit Score:** {credit_score}")
    st.write(f"**Rating:** {rating}")

    # Textual Inference Section
    st.write("### Summary")
    if probability < 0.2:
        st.write("The customer has a **low risk** of defaulting on the loan.")
    elif 0.2 <= probability < 0.5:
        st.write(
            "The customer has a **moderate risk** of defaulting on the loan. Additional analysis might be required.")
    else:
        st.write("The customer has a **high risk** of defaulting on the loan. Loan approval should be reconsidered.")

    if credit_score >= 750:
        st.write("The customer's **credit score is excellent**, suggesting strong financial reliability.")
    elif 650 <= credit_score < 750:
        st.write("The customer's **credit score is average**, indicating some financial reliability.")
    else:
        st.write("The customer's **credit score is poor**, highlighting potential financial risks.")

    st.write(f"The customer is rated as **{rating}**, reflecting their overall financial profile.")
