import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("customer_churn.csv")


print("First 5 Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nSummary Statistics:")
print(df.describe())

print("\nCustomer Churn Count:")
print(df["Churn"].value_counts())

print("\nAverage Tenure:")
print(np.mean(df["tenure"]))

print("\nAverage Monthly Charges:")
print(np.mean(df["MonthlyCharges"]))

sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Count")
plt.show()

sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges vs Churn")
plt.show()

sns.histplot(data=df, x="tenure", hue="Churn", bins=20)
plt.title("Customer Tenure Distribution")
plt.show()

sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Contract Type vs Customer Churn")
plt.xticks(rotation=20)
plt.show()
