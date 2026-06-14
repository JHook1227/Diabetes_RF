import pandas as pd


db_diabetes = pd.read_csv("Diabetes_Health_Burden.csv")

#db_diabetes.head()

#db_diabetes.info()

#db_diabetes.describe()

attribute_1 = db_diabetes["Short Indicator Text"].unique()

SIT = ['Peripheral Vascular Disease', 'High Blood Pressure', 'Chronic Kidney Disease', 
    'Coronary Heart Disease', 'Diabetic Ketoacidosis', 'Mobility Limitations', 
    'High Cholesterol', 'Limitations in Instrumental Activities of Daily Living', 
    'Stroke', 'Diabetes Prevalence', 'Diabetes Incidence', 'Congestive Heart Failure',
    'Lower Extremity Amputations', 'Myocardial Infarction', 'Hypoglycemia' ,'Severe Vision Impairment or Blindness'
    'Hyperosmolar Hyperglycemic Nonketotic Syndrome']



attribute_2 = db_diabetes["Long Indicator Text"].unique()

LIT = ['Prevalence of Peripheral Vascular Disease in Medicare Beneficiaries with Diabetes, Aged 65 Years or Older',
 'Prevalence of Self-reported High Blood Pressure in Adults with Diabetes, Aged 18 Years or Older',
 'Prevalence of Chronic Kidney Disease in Medicare Beneficiaries with Diabetes, Aged 65 Years or Older',
 'Prevalence of Self-reported Coronary Heart Disease in Adults with Diabetes, Aged 18 Years or Older',
 'Hospitalizations for Diabetic Ketoacidosis as First-Listed Diagnosis in Adults with Diabetes',
 'Prevalence of Self-reported Mobility Limitations in Adults with Diabetes, Aged 18 Years or Older',
 'Prevalence of Self-reported High Cholesterol in Adults with Diabetes, Aged 18 Years or Older',
 'Prevalence of Self-reported Limitations in Instrumental Activities of Daily Living (IADL) in Adults with Diabetes, Aged 18 Years or Older',
 'Hospitalizations for Stroke as First-Listed Diagnosis in Adults with Diabetes',
 'Prevalence of Self-reported Diagnosed Diabetes in Adults, Aged 18 Years or Older',
 'Incidence of Diagnosed Diabetes in Adults, Aged 18-76 Years Old',
 'Hospitalizations for Congestive Heart Failure as First-Listed Diagnosis in Adults with Diabetes',
 'Hospitalizations for Lower Extremity Amputations in Adults with Diabetes',
 'Hospitalizations for Myocardial Infarction as First-Listed Diagnosis in Adults with Diabetes',
 'Hospitalizations for Hypoglycemia as First-Listed Diagnosis in Adults with Diabetes',
 'Prevalence of Congestive Heart Failure in Medicare Beneficiaries with Diabetes, Aged 65 Years or Older',
 'Prevalence of Coronary Heart Disease in Medicare Beneficiaries with Diabetes, Aged 65 Years or Older',
 'Prevalence of Self-reported Severe Vision Impairment or Blindness in Adults with Diabetes, Aged 18 Years or Older',
 'Hospitalizations for Hyperosmolar Hyperglycemic Nonketotic Syndrome as First-Listed Diagnosis in Adults with Diabetes']

attribute_3 = db_diabetes["Stratification 1"].unique()

Strat_1 = ['Sex', 'Age', 'Income', 'Race-Ethnicity', 'Rural and Urban Areas', 'Education']

attribute_4 = db_diabetes["Stratification Group 1"].unique()

Strat_1_Group = ['Overall', 'Females', 'Males', 'Low Income (<$35k)', 'Hispanic',
                 'Non-Hispanic Black', 'Non-Hispanic Other Races', 'Rural', 'Urban',
                 'Rural Areas', 'More than high school', 'Urban Areas',
                 'Less than high school', 'Low income (<$35k)', 'Middle Income ($35-<$75k)',
                 'High school graduate or General Educational Development (GED) holder',
                 'Non-Hispanic White', 'High Income ($75k+)']

attribute_5 = db_diabetes["Stratification 2"].unique()

Strat_2 = ['Age']

attribute_6 = db_diabetes["Stratification Group 2"].unique()

Strate_2_Group = ['65-74','75+','65+','18+','18-64','18-44','45-64']


attribute_7 = db_diabetes["Stratification Group 2 Label"].unique()

data_types = db_diabetes["Data Type"].unique()

types = ['Total Cases', 'Crude Rate (per 100)', 'Estimated Cases (in thousands)',
         'Total Events', 'Age-adjusted Rate (per 100)',
         'Estimated Cases Attributable to Diabetes (in thousands)',
         'Crude Rate (per 1,000)', 'Age-adjusted Rate (per 1,000)', 'Rate (per 100)',
         'Number of Cases (in thousands)',
         'Estimated Events Attributable to Diabetes', 'Total Cases (in thousands)', 'Age-adjusted Rate', 'Crude Rate']



amputation_db = db_diabetes[db_diabetes["Short Indicator Text"] == "Lower Extremity Amputations"]

amp_data_types = amputation_db["Data Type"].unique()
amp_types = ['Total Events', 'Estimated Events Attributable to Diabetes',
             'Crude Rate (per 1,000)', 'Age-adjusted Rate (per 1,000)']

print(amputation_db["Stratification Group 1"].value_counts())