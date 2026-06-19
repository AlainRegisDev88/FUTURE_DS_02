import pandas as pd
import openpyxl

unclean_df = pd.read_csv('./data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

df = unclean_df.dropna().drop_duplicates()


# df.to_excel('./excel.xlsx')

print(df.head(10))


# totals data
total_customers = df['customerID'].count()
churn_true = (df['Churn'] == 'Yes').sum()

# Partners
partners = df[df['Partner'] == 'Yes']
not_partners = df[df['Partner'] == 'No']

# dependents
dependents = df[df['Dependents'] == 'Yes']
non_dependents = df[df['Dependents'] == 'No']


# senior_citizens
senior_citizens = df[df['SeniorCitizen'] == '1']

# Organise by contract type
contract_type = df.groupby('Contract')[['Churn']].count()


# organise by tenure
tenure  =df.groupby('tenure')[['tenure', 'Churn']]

# organize by phone service availability
phone_service = df.groupby('PhoneService')[['PhoneService', 'Churn']]

#CHURN RATES

total_churn_rate = round((( churn_true / total_customers) * 100), 2)

# by partners
churn_rate_partners = round((((partners['Churn'] == 'Yes').mean()) * 100), 2)
print(churn_rate_partners)
# by non_partners
churn_rate_non_partners = round((((not_partners['Churn'] == 'Yes').mean()) * 100), 2)
print(churn_rate_non_partners)




# RETENTION RATES

total_retention_rate = 100 - total_churn_rate


