import pandas as pd
import openpyxl

unclean_df = pd.read_csv('./data/WA_Fn-UseC_-Telco-Customer-Churn.csv')

df = unclean_df.dropna().drop_duplicates()


df.to_excel('./excel.xlsx')

print(df.head(10))


total_customers = df['customerID'].count()
churn_true = (df['Churn'] == 'Yes').sum()
print(total_customers)
print(churn_true)

# Partners

partners = df[df['Partner'] == 'Yes']
dependents = df[df['Dependents'] == 'Yes']
senior_citizens = df[df['SeniorCitizen'] == '1']


print(partners.head())
print(df.info())

churn_rate = round((( churn_true / total_customers) * 100), 2)
print(churn_rate)

retention_rate = 100 - churn_rate

churn_by_partnership = df.groupby('Partner')[['Partner','Churn']]
print(churn_by_partnership.head(5))




