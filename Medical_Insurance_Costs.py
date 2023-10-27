# The point of this project is to draw conclusions from a dataset using data analysis tools in Python.
# The dataset used is the 'Medical Cost Personal Dataset' from Kaggle. It has been cleaned already.

import pandas as pd

df = pd.read_csv('insurance.csv')
print(df.head(10))

# Find the average age of patients.
avg_age = df.age.mean()
print('The average age is: ' + str(avg_age))

'''
The average age of participants is 39.
'''

# Group the data by male and female.
grouped_df = df.groupby('sex').sex.count()
print(grouped_df)

'''
There are a few more males but it is nearly even. Let's take a look at the costs for males vs females.
'''

# Find the average charge costs of male/female who smoke and don't smoke.
avg_charge = df.groupby(['sex', 'smoker']).charges.mean().reset_index()

# Create a pivot table using the dataframe above.
avg_charge_pivot = avg_charge.pivot(
    columns='smoker',
    index='sex',
    values='charges')
print(avg_charge_pivot)

'''
Based on the data, smokers have higher charges on average for both genders. 
Male smokers have higher costs than female smokers but female non-smokers have higher costs 
than male non-smokers. 
'''

# Group the patients into age ranges and take the average of those age ranges
# Define age groups and their labels to categorize the ages.
age_bins = [18, 30, 42, 54, 64]
age_labels = ['18-29', '30-41', '42-53', '54-64']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Group the dataframe by age group and smoker and take the average cost for each age range and
# find the ratio of the non-smoker to smoker charges for each age group.
grouped_avg = df.groupby(['age_group', 'smoker']).charges.mean().unstack(fill_value=0)
grouped_avg['ratio'] = grouped_avg['no'] / grouped_avg['yes']

print(grouped_avg)

'''
Charges increase along with age for both smokers and non-smokers. 
We also see that charges are greater for all smokers, regardless of age.

Something interesting is that the charges for the 18-29 group of smokers 
is over 6x the charges for non-smokers in that same age range while 
charges for smokers in the 54-64 age range are a little under 3x the
charges for non-smokers in that same age range. 

According to the data, younger smokers face many more charges compared to
their counterparts. 
'''

