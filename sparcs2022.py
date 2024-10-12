import numpy as np

import pandas as pd

import polars as pl

import matplotlib.pyplot as plt

import seaborn as sns



### (1) Load the Data:
df = pd.read_csv('sparcs2022_inpatient.csv')

print(df.head()) # print the first 5 rows
print(df) # print the entire dataframe
print(df.columns) # print the column names


## --> Cleaning the data:
## remove all whitespace, lower case, replace space with underscore from column names:
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_')
df_len = len(df)


df.total_charges = df.total_charges.apply(lambda x: x.replace(',', ''))
df.total_costs = df.total_costs.apply(lambda x: x.replace(',', ''))


## Convert the Necessary Categories to Numeric:
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')


##-->Count NaN for Total Charges and Total Costs:
df['length_of_stay'].isna().sum()
df['total_charges'].isna().sum()
df['total_costs'].isna().sum()


## (2) Explore the Necessary Data Columns:
df = df[['age_group', 'length_of_stay', 'total_charges', 'total_costs', 'type_of_admission', 'gender']]

print(df.head()) # print the first 5 rows
print(df.tail()) # print the last 5 rows
print(df) # print the entire dataframe


## --> Explore each Categorical Variable:

# ➤Age Group Distribution:
age_group = df['age_group'].value_counts()
print(age_group)

# ★Age Group Bar Plot:

plt.figure(figsize=(12, 8))
sns.barplot(x=age_group.index, y=age_group.values, palette='Purples')
plt.title('Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.show()


# ➤Gender Distribution:

gender = df['gender'].value_counts()
print(gender)

# ★Gender Bar Plot:

plt.figure(figsize=(12, 8))
sns.barplot(x=gender.index, y=gender.values, palette='Blues')
plt.title('Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.75)
plt.show()


# ➤Type of Admission Distribution:

admissiontype = df['type_of_admission'].value_counts()
print(admissiontype)

# ★Type of Admission Bar Plot:

plt.figure(figsize=(12, 8))
admissiontype.plot(kind='bar', color=['purple', 'skyblue', 'hotpink', 'lightpink', 'blue', 'orange'])
plt.title('Distribution by Admission Type')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

## -->Exploring Other Categorical Variable: [Length of Stay, Total Charges, Total Costs, and Type of Admission]

# ➤Length of Stay:
length_of_stay = df['length_of_stay'].value_counts()
print(length_of_stay)

# ➤Total Charges:
totalcharges = df['total_charges'].value_counts()
print(totalcharges)

# ➤Total Costs:
totalcosts = df['total_costs'].value_counts()
print(totalcosts)

# ➤Type of Admission:
admissiontype = df['type_of_admission'].value_counts()
print(admissiontype)

## change default display options to not display exponential notation but float
pd.set_option('display.float_format', lambda x: '%.3f' % x)


### (3) Perform Descriptive Statistics:
## Descriptive Statistics for the Entire Dataframe:
descriptive = df[['length_of_stay', 'total_charges', 'total_costs']].describe()
print(descriptive)

## Descriptive Statistics for each Categorical Data:
descriptive = df['length_of_stay'].describe()
print(descriptive)

descriptive = df['total_charges'].describe()
print(descriptive)

descriptive = df['total_costs'].describe()
print(descriptive)



### (4) Data Visualization:

## Histogram of Length of Stay: Distribution of hospital stay durations.

plt.figure(figsize=(12, 8))
plt.hist(df['length_of_stay'], bins=15, color='grey', edgecolor='black')
plt.title('Hospital Duration')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.show()



## Boxplot for Total Charges: Potential outliers in the cost of care.

plt.figure(figsize=(10, 9))
sns.boxplot(x=df['total_charges'], color='orange')
plt.title('Total Charges in the Cost of Care')
plt.xlabel('Total Charges')
plt.show()



## Bar Plot for Type of Admission: Provides insights into the frequencies of different reasons of admission.

admissiontype = df['type_of_admission'].value_counts()
plt.figure(figsize=(12, 8))
admissiontype.plot(kind='bar', color='tan')
plt.title('Distribution by Admission Type')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



### (5) Missing Data:

## -->Check for missing data (each column):
missingdata = df.isnull().sum()
print(missingdata)


## -->How to handle missing data:

## (a.) Drop Rows with Missing Data in Specific Columns:

drop = df.dropna()
print("Data after dropping rows with missing data:\n", drop.isnull().sum())

## (b.) Fill Missing Data (Mean): for numeric columns

filled_mean = df.fillna(df.mean())
print("Data after filling missing data with mean:\n", filled_mean.isnull().sum())  #this took a long time to run and i couldn't wait for it to finish!


## (c) Verify missing data was handled:

print("Data after filling missing data with mean:\n", df.isnull().sum())


### (6) Summary Report:

# ★What is the Average Length of Stay?

length_of_stay = df['length_of_stay'].mean()
print(f"Average Length of Stay: {length_of_stay:.2f} days")


# ★Total Cost Variation (Age Group)★

age_group_cost = df.groupby('age_group')['total_costs'].mean()
print(age_group_cost)

print(f"Total Cost by Age Group:\n{age_group_cost}")

# Total Cost by Age Group Visualization:
plt.figure(figsize=(10, 6))
sns.barplot(x=age_group_cost.index, y=age_group_cost.values, palette='Purples')
plt.title('Average Total Cost by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Total Cost')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ★Total Cost Variation (Type of Admission)★

admissiontype_cost = df.groupby('type_of_admission')['total_costs'].mean()
print("Total Cost by Type of Admission:\n", admissiontype_cost)

# Total Cost by Type of Admission Visualization:
plt.figure(figsize=(10, 6))
sns.barplot(x=admissiontype_cost.index, y=admissiontype_cost.values, palette='Purples')
plt.title('Total Cost by Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Average Total Cost')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# ★Noticeable Trends★

admissiontype = df['type_of_admission'].value_counts()
print(admissiontype)


admissiontype = df['type_of_admission'].value_counts()
plt.figure(figsize=(12, 8))
sns.barplot(x=admissiontype.index, y=admissiontype.values, palette='pink')
plt.title('Distribution by Admission Type')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

