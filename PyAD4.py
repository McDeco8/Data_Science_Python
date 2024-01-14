#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# All Imp Predefined Function in Data science python


# In[ ]:


# Numpy Function

import numpy as np

data = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(data)
print(mean_value)


# In[ ]:


import numpy as np

data = np.array([1, 2, 3, 4, 5])
std_dev = np.std(data)
print(std_dev)


# In[ ]:


import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())


# In[ ]:


# Pandas Function
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())


# In[ ]:


import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
statistics = df.describe()
print(statistics)


# In[ ]:


# Scikit-Learn Function

from sklearn.model_selection import train_test_split

X, y = data[['feature1', 'feature2']], data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)


# In[ ]:


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)


# In[ ]:


from sklearn.metrics import confusion_matrix

y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)


# In[ ]:





# In[ ]:




