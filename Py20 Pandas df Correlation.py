#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Example 1: Pearson correlation
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 1, 2, 1]}

df = pd.DataFrame(data)

# Calculate Pearson correlation matrix
correlation_matrix = df.corr(method='pearson')
print("Pearson Correlation Matrix:")
print(correlation_matrix)


# In[2]:


import pandas as pd

# Example 2: Spearman rank correlation
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 1, 2, 1]}

df = pd.DataFrame(data)

# Calculate Spearman rank correlation matrix
correlation_matrix_spearman = df.corr(method='spearman')
print("Spearman Rank Correlation Matrix:")
print(correlation_matrix_spearman)


# In[3]:


import pandas as pd

# Example 3: Kendall rank correlation
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 1, 2, 1]}

df = pd.DataFrame(data)

# Calculate Kendall rank correlation matrix
correlation_matrix_kendall = df.corr(method='kendall')
print("Kendall Rank Correlation Matrix:")
print(correlation_matrix_kendall)


# In[4]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example 4: Correlation heatmap
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 1, 2, 1]}

df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title("Correlation Heatmap")
plt.show()


# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example 5: Pairwise scatter plots
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [1, 2, 1, 2, 1]}

df = pd.DataFrame(data)

# Create pairwise scatter plots
sns.pairplot(df)
plt.suptitle("Pairwise Scatter Plots", y=1.02)
plt.show()

