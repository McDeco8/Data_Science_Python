#!/usr/bin/env python
# coding: utf-8

# In[1]:


## SET and set methods


# In[2]:


# Example 1: Creating a set
fruits = {'apple', 'banana', 'cherry', 'orange'}
print(fruits)


# In[3]:


# Example 2a: Adding an element to a set
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)


# In[4]:


# Example 2b: Removing an element from a set
fruits = {'apple', 'banana', 'cherry', 'orange'}
fruits.remove('banana')
print(fruits)


# In[5]:


# Example 3a: Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)


# In[6]:


# Example 3b: Intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print(intersection_set)


# In[7]:


# Example 4a: Removing and returning an arbitrary element using pop()
fruits = {'apple', 'banana', 'cherry', 'orange'}
removed_fruit = fruits.pop()
print(f"Removed fruit: {removed_fruit}")
print(fruits)


# In[8]:


# Example 4b: Clearing all elements from a set
fruits = {'apple', 'banana', 'cherry', 'orange'}
fruits.clear()
print(fruits)


# In[9]:


# Example 5a: Checking if an element is present in a set
fruits = {'apple', 'banana', 'cherry', 'orange'}
if 'banana' in fruits:
    print("Banana is in the set.")


# In[10]:


# Example 5b: Checking if a set is a subset of another set
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(f"Is set1 a subset of set2? {is_subset}")


# In[ ]:




