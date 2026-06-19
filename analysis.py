import pandas as pd
import openpyxl

unclean_df = pd.read_csv('./data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

df = unclean_df.dropna().drop_duplicates()



#UTILS
df['has_churned'] =  df['Churn'] == 'Yes'
# df.to_excel('./excel.xlsx')



print(df.head(10))


# totals data
total_customers = df['customerID'].count()
churn_true = (df['Churn'] == 'Yes').sum()

# Partners
partners = df[df['Partner'] == 'Yes']
non_partners = df[df['Partner'] == 'No']

# dependents
dependents = df[df['Dependents'] == 'Yes']
non_dependents = df[df['Dependents'] == 'No']


# senior_citizens
senior_citizens = df[df['SeniorCitizen'] == 1]
non_senior_citizens = df[df['SeniorCitizen'] == 0]

# Organise by contract type
contract_type = df.groupby('Contract')[['Churn']].count()


# organise by tenure
tenure  =df.groupby('tenure')[['tenure', 'Churn']]

# organize by phone service availability
phone_service = df.groupby('PhoneService')[['PhoneService', 'Churn']]

#CHURN RATES

total_churn_rate = round((( churn_true / total_customers) * 100), 2)
print(f"{"="*10}CHURN RATES{"="*10}")
# by partners
churn_rate_partners = round((((partners['Churn'] == 'Yes').mean()) * 100), 2)
print("Partners: ", churn_rate_partners)
# by non_partners
churn_rate_non_partners = round((((non_partners['Churn'] == 'Yes').mean()) * 100), 2)
print("Non Partners:", churn_rate_non_partners)

# by dependents
churn_rate_dependents = round((((dependents['Churn'] == 'Yes').mean()) * 100), 2)
print("Dependents: ", churn_rate_dependents)
#by non-dependent people
churn_rate_non_dependents = round((((non_dependents['Churn'] == 'Yes').mean()) * 100), 2)
print("Non-dependents: ", churn_rate_non_dependents)

# by senior citizens
churn_rate_senior_citizens = round((((senior_citizens['Churn'] == 'Yes').mean()) * 100), 2)
print("Seniors: ",churn_rate_senior_citizens)
# by younger people
churn_rate_non_senior_citizens = round((((non_senior_citizens['Churn'] == 'Yes').mean()) * 100), 2)
print("Young: ",churn_rate_non_senior_citizens)

# contract type
print(contract_type.head(5))

# churn rates by contract
churn_rates_by_contract_type = ((df.groupby('Contract')['has_churned'].mean()) * 100).round(2)
print(churn_rates_by_contract_type)






# RETENTION RATES

total_retention_rate = 100 - total_churn_rate


