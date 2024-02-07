#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Example 1: Calculating mean and sum
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'Salary': [50000, 60000, 45000]}

df = pd.DataFrame(data)

# Calculate mean and sum for the 'Age' and 'Salary' columns
aggregated_data = df.agg({'Age': 'mean', 'Salary': 'sum'})
print("Aggregated Data (mean Age, sum Salary):")
print(aggregated_data)


# In[2]:


import pandas as pd

# Example 2: GroupBy aggregation
data = {'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco'],
        'Population': [8500000, 884000, 3990000, 8500000, 884000]}

df = pd.DataFrame(data)

# Group by 'City' and calculate mean population for each city
grouped_data = df.groupby('City')['Population'].mean()
print("GroupBy Aggregated Data (mean Population for each City):")
print(grouped_data)


# In[3]:


import pandas as pd

# Example 3: Aggregating with custom functions
data = {'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco'],
        'Population': [8500000, 884000, 3990000, 8500000, 884000]}

df = pd.DataFrame(data)

# Define a custom function for aggregation
def population_range(series):
    return series.max() - series.min()

# Group by 'City' and apply custom aggregation function
aggregated_data_custom = df.groupby('City')['Population'].agg(population_range)
print("Custom Aggregated Data (Population range for each City):")
print(aggregated_data_custom)


# In[4]:


import pandas as pd

# Example 4: Counting unique values
data = {'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco'],
        'Population': [8500000, 884000, 3990000, 8500000, 884000]}

df = pd.DataFrame(data)

# Count unique values in the 'City' column
unique_counts = df['City'].value_counts()
print("Unique Counts for each City:")
print(unique_counts)


# In[5]:


import pandas as pd

# Example 5: Aggregating multiple statistics
data = {'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco'],
        'Population': [8500000, 884000, 3990000, 8500000, 884000],
        'Area': [468.9, 121.4, 468.7, 468.9, 121.4]}

df = pd.DataFrame(data)

# Group by 'City' and calculate mean and sum for 'Population' and 'Area'
aggregated_data_multiple = df.groupby('City').agg({'Population': ['mean', 'sum'], 'Area': 'sum'})
print("Aggregated Data (mean and sum for Population, sum for Area):")
print(aggregated_data_multiple)

