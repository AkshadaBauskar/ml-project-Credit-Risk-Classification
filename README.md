# Credit Risk Modeling

This project involves developing a Credit Risk Model to assist any NBFC Finance company, in assessing the creditworthiness of loan applicants. It includes a predictive model, a scoring system, and a Streamlit-based user interface to predict default probabilities and categorize credit risk.

---

## Project Overview

### Objective
- Build a predictive model to assess credit risk and provide a scoring system.
- Create a user-friendly application for real-time assessment of loan applications.

### Key Deliverables
1. **Credit Risk Model**: Predict default probabilities.
2. **Scorecard**: Categorize loans into Poor, Average, Good, and Excellent.
3. **Streamlit App**: Provide a user-friendly interface for loan officers.

---

## Features

### Input Variables
- **Demographics**: Age, residence type, income, etc.
- **Loan Details**: Loan amount, tenure, purpose, type, etc.
- **Credit History**: Delinquency ratio, credit utilization, open accounts, etc.

### Output Variables
- **Default Probability**: Likelihood of default.
- **Credit Score**: Numerical score indicating creditworthiness.
- **Rating**: Categorization into Poor, Average, Good, or Excellent.

---

## Technical Implementation

### Modeling Steps
1. **Preprocessing**:
   - Handle missing values and outliers.
   - Scale numerical features using Min-Max Scaling.
   - Perform feature selection using IV, VIF, and domain knowledge.
2. **Model Training**:
   - Algorithms: Logistic Regression, Random Forest, XGBoost.
   - Hyperparameter Tuning: RandomizedSearchCV, Optuna.
3. **Evaluation**:
   - Metrics: AUC, Gini, KS Statistic, Classification Report.

### Tools and Technologies
- **Programming**: Python
- **Libraries**: Pandas, Scikit-learn, XGBoost, Joblib, Streamlit
- **UI**: Streamlit for real-time predictions

---

## Streamlit Application

### Features
1. Input customer demographics, loan details, and credit history.
2. Predict default probability, credit score, and risk rating.
3. Display input summary and detailed textual inference.

### Run the Application
```bash
streamlit run app/main.py
```

### Example Usage

**Input**:  
- Age: 35  
- Income: ₹850,000  
- Loan Amount: ₹1,200,000  

**Output**:  
- **Default Probability**: 15.2%  
- **Credit Score**: 780  
- **Rating**: Good  

---

### Performance

**Model Metrics**:
- **AUC**: 98%  
- **Gini**: 96%  
- **KS Statistic**: 85.98% (within first three deciles)  

---

### Insights

1. Young and older individuals have a slightly higher risk of default.
2. High income and large sanctioned amounts lower the default probability.
3. Higher credit utilization and delinquency ratios increase the default risk.

---

### Future Enhancements

#### Phase 2: Monitoring and MLOps
1. Implement real-time model performance monitoring.  
2. Automate processes for high-confidence applications.

