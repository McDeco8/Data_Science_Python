#!/usr/bin/env python
# coding: utf-8

# In[1]:


# #Strings and its methods


# In[2]:


# Example 1: Creating and concatenating strings
str1 = 'Hello'
str2 = 'World'
concatenated_str = str1 + ' ' + str2
print(concatenated_str)


# In[10]:


# Example 2a: String formatting with the % operator
name = 'Alice'
age = 25
formatted_str = 'My name is %s and I am %d years old.' % (name, age)
print(formatted_str)


# In[4]:


# Example 2b: String formatting with the format() method
name = 'Bob'
age = 30
formatted_str = 'My name is {} and I am {} years old.'.format(name, age)
print(formatted_str)


# In[5]:


# Example 3a: Converting to lower and upper case
text = 'Python is Fun'
lower_case = text.lower()
upper_case = text.upper()
print(f"Lower case: {lower_case}, Upper case: {upper_case}")


# In[6]:


# Example 3b: Splitting a string into a list of substrings
sentence = 'This is a sample sentence.'
words = sentence.split()
print(words)


# In[7]:


# Example 4: String slicing and indexing
text = 'Python Programming'
substring1 = text[0:6]
substring2 = text[7:]
print(f"Substring 1: {substring1}, Substring 2: {substring2}")


# In[8]:


# Example 5b: Replacing a substring in a string
sentence = 'Python is easy and Python is fun.'
modified_sentence = sentence.replace('Python', 'Java')
print(modified_sentence)


# In[ ]:





# In[ ]:





# In[ ]:




