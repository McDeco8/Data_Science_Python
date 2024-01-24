#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from array import array

# Example 1: Creating an array of integers
integer_array = array('i', [1, 2, 3, 4, 5])
print(integer_array)


# In[ ]:


from array import array

# Example 2: Accessing elements and array operations
float_array = array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
print(float_array[2])  # Accessing element at index 2
float_array.append(6.6)  # Appending a new element
print(float_array)


# In[ ]:


import numpy as np

# Example 3: Creating a NumPy array
numpy_array = np.array([1, 2, 3, 4, 5])
print(numpy_array)


# In[ ]:


import numpy as np

# Example 4: NumPy array operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2  # Element-wise addition
print(result)

matrix = np.array([[1, 2], [3, 4]])
transpose_matrix = np.transpose(matrix)  # Transposing a matrix
print(transpose_matrix)


# In[ ]:


import numpy as np

# Example 5: NumPy array methods
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
unique_values = np.unique(arr)  # Finding unique values
sorted_values = np.sort(arr)  # Sorting array elements
print(unique_values)
print(sorted_values)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




