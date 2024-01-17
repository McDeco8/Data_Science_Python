#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Tuples and various Tuple methods in Python:


# In[2]:


# Example 1: Creating a tuple
fruits = ('apple', 'banana', 'cherry', 'orange')
print(fruits)


# In[3]:


# Example 2a: Accessing elements using indexing
fruits = ('apple', 'banana', 'cherry', 'orange')
first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")


# In[4]:


# Example 2b: Accessing elements using negative indexing
fruits = ('apple', 'banana', 'cherry', 'orange')
last_fruit = fruits[-1]
print(f"Last fruit: {last_fruit}")


# In[5]:


# Example 3: Concatenating tuples
fruits1 = ('apple', 'banana')
fruits2 = ('cherry', 'orange')
combined_fruits = fruits1 + fruits2
print(combined_fruits)


# In[8]:


# Example 4a: Counting occurrences of an element in a tuple
numbers = (1, 2, 3, 4, 2,1,2,2,1,5,4,3,2,3,1,5,5, 5, 2)
count_of_2 = numbers.count(5)
print(f"Count of 2: {count_of_2}")


# In[9]:


# Example 4b: Finding the index of an element in a tuple
numbers = (1, 2, 3, 4, 5)
index_of_4 = numbers.index(4)
print(f"Index of 4: {index_of_4}")


# In[10]:


# Example 5: Nested tuples
coordinates = ((1, 2), (3, 4), (5, 6))
print(coordinates)


# In[ ]:





# In[ ]:





# In[ ]:




