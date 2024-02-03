#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Example 1: Selecting columns
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Selecting a single column
name_column = df['Name']
print("Name Column:")
print(name_column)

# Selecting multiple columns
selected_columns = df[['Name', 'Age']]
print("\nSelected Columns:")
print(selected_columns)


# In[2]:


import pandas as pd

# Example 2: Selecting rows based on conditions
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Selecting rows where Age is greater than 25
selected_rows = df[df['Age'] > 25]
print("Selected Rows where Age > 25:")
print(selected_rows)


# In[3]:


import pandas as pd

# Example 3: Selecting specific cells
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Selecting a specific cell using loc
cell_value = df.loc[1, 'Age']
print("Cell Value at Row 1, Column 'Age':", cell_value)


# In[4]:


import pandas as pd

# Example 4: Selecting rows by index
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Selecting rows by index
selected_rows = df.loc[[0, 2]]
print("Selected Rows by Index:")
print(selected_rows)


# In[5]:


import pandas as pd

# Example 5: Using iloc for integer-based indexing
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

# Selecting rows and columns using iloc
selected_data = df.iloc[1:3, 0:2]
print("Selected Data using iloc:")
print(selected_data)

