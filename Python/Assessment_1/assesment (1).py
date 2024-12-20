# -*- coding: utf-8 -*-
"""Assesment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tcxWQ0PaNKqz8YQpVaHg4Q7GdKpU-gbe

**Python Assesment 1**

1) Import pandas and read in the banklist.csv file into a dataframe called
banks.
"""

import numpy as np
import pandas as pd
banks = pd.read_csv('banklist.csv')
banks

"""2) Show the head of the dataframe"""

banks.head()

"""3) What are the column names?"""

1 Bank Name
2 city
3 ST
4 convert_from_missing_indexer_tuple
5 acquiring_insitutions
6 Closing date
7 Updated date

"""4) How many States (ST) are represented in this data set?

"""

# There are 44 unique states (ST) represented in the dataset.

"""5) Get a list or array of all the states in the data set"""

states_list = banks['ST'].unique()
states_list

"""6) What are the top 5 states with the most failed banks?


"""

state_count = banks['ST'].value_counts()
top_5_states = state_count.head(5)
top_5_states

"""7) What are the top 5 acquiring institutions?"""

acquiring_insitutions = banks['Acquiring Institution'].value_counts()
top_5_acquiring_insitutions = acquiring_insitutions.head(5)
top_5_acquiring_insitutions

"""8) How many banks has the State Bank of Texas acquired? How many of
them were actually in Texas?
"""

state_bank_of_texas = banks[banks['Acquiring Institution'] == 'State Bank of Texas']
banks_acquired_by_state_bank_of_texas = state_bank_of_texas['Bank Name'].nunique()
banks_acquired_by_state_bank_of_texas

"""9) What is the most common city in California for a bank to fail in?"""

city = banks[banks['ST'] == 'CA']
most_common_city = city['City'].value_counts().idxmax()
most_common_city

"""**Python Assesment 2**

Q 1: Develop a Line chart using the functionality of pandas to show how
automobile sales fluctuate from year to year.
"""

import pandas as pd
df = pd.read_csv('historical_automobile_sales.csv')
df

import pandas as pd
import matplotlib.pyplot as plt
# Assuming 'df' is your DataFrame with 'Year' and 'Automobile_Sales' columns
plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Automobile_Sales'],color='purple')
plt.title('Yearly Automobile Sales')
plt.xlabel('Year')
plt.ylabel('Total Automobile Sales')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df['Advertising_Expenditure'], df['Automobile_Sales'], color='green')

plt.title('Box Plot of Automobile Sales')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.show()

"""Q.2
Plot different lines for categories of vehicle type and analyze the trend
to answer the question Is there a noticeable difference in sales trends
between different vehicle types during recession periods?
"""

import pandas as pd
import matplotlib.pyplot as plt

# Filter data for recession periods
recession_data = df[df['Recession'] == 1]

# Pivot the data to have years as the index and vehicle types as columns
pivot_data = recession_data.pivot_table(values='Automobile_Sales', index='Year', columns='Vehicle_Type')

# Plotting the line chart
pivot_data.plot(kind='line', marker='o', figsize=(12, 8))

plt.title('Automobile Sales Trends by Vehicle Type During Recession Periods')
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.legend(title='Vehicle Type')
plt.show()

"""Q 3: Use the functionality of Seaborn Library to create a visualization to compare
the sales trend per vehicle type for a recession period with a non- recession
period.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,8))
sns.lineplot(data=df, x='Year', y='Automobile_Sales', hue='Vehicle_Type',style='Recession', markers=True,dashes=False)
plt.title('Automobile Sales Trends by Vehicle Type')
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.grid(True)
plt.show()

"""Q 4: Now you want to compare the sales of different vehicle types
during a recession and a non-recession period
"""

aggregated_data = df.groupby(['Vehicle_Type', 'Recession'])['Automobile_Sales'].mean().reset_index()
aggregated_data

# Plotting
plt.figure(figsize=(8, 6))
sns.barplot(x='Vehicle_Type', y='Automobile_Sales', hue='Recession', data=aggregated_data)
plt.title('Average Automobile Sales During Recession vs Non-Recession')
plt.xlabel('Vehicle Type')
plt.ylabel('Average Sales')
plt.legend(title='Recession Period', labels=['Non-Recession', 'Recession'])
plt.tight_layout()
plt.show()