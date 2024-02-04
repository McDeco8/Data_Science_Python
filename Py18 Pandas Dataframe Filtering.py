#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Example 1: Simple column value filtering
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Filter rows where Age is greater than 25
filtered_data = df[df['Age'] > 25]
print("Filtered Data where Age > 25:")
print(filtered_data)


# In[2]:


import pandas as pd

# Example 2: Multiple conditions with logical operators
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Filter rows where Age is greater than 25 and City is 'New York'
filtered_data = df[(df['Age'] > 25) & (df['City'] == 'New York')]
print("Filtered Data with Age > 25 and City is 'New York':")
print(filtered_data)


# In[3]:


import pandas as pd

# Example 3: String contains filtering
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Filter rows where City contains 'Los'
filtered_data = df[df['City'].str.contains('Los')]
print("Filtered Data where City contains 'Los':")
print(filtered_data)


# In[4]:


import pandas as pd

# Example 4: Filtering with isin
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Filter rows where City is either 'New York' or 'Los Angeles'
filtered_data = df[df['City'].isin(['New York', 'Los Angeles'])]
print("Filtered Data where City is 'New York' or 'Los Angeles':")
print(filtered_data)


# In[5]:


import pandas as pd

# Example 5: Filtering null (NaN) values
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, 22, None],
        'City': ['New York', 'San Francisco', 'Los Angeles', None]}

df = pd.DataFrame(data)

# Filter rows with non-null values in the 'Name' column
filtered_data = df[df['Name'].notna()]
print("Filtered Data with non-null values in the 'Name' column:")
print(filtered_data)

