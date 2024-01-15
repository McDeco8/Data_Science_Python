#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## LIST in PYTHON and List Method


# In[1]:


# Example 1: Creating a list
fruits = ['apple', 'banana', 'cherry', 'orange']
print(fruits)


# In[2]:


# Example 2a: Appending an element to the list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)


# In[3]:


# Example 2b: Extending the list with another list
fruits = ['apple', 'banana', 'cherry']
additional_fruits = ['orange', 'kiwi']
fruits.extend(additional_fruits)
print(fruits)


# In[4]:


# Example 3a: Removing a specific element from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.remove('banana')
print(fruits)


# In[5]:


# Example 3b: Removing an element by index using pop()
fruits = ['apple', 'banana', 'cherry', 'orange']
removed_fruit = fruits.pop(1)
print(fruits)
print(f"Removed fruit: {removed_fruit}")


# In[6]:


# Example 4: List slicing
numbers = [1, 2, 3, 4, 5]
subset = numbers[1:4]
print(subset)


# In[7]:


# Example 5: List comprehension to create a new list
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




