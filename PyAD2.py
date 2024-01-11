#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Conditional statment in python


# In[4]:


# Example 1: If statement
a = 3

if a > 0:
    print("Entered number is Positive ")


# In[ ]:


# Example 2: If-else statement
b = -5

if b > 0:
    print("y is a positive number.")
else:
    print("y is either zero or a negative number.")


# In[6]:


# Example 3: If-elif-else statement
grade = 86

if grade >= 90:
    print("Grade:A")
elif 80 <= grade < 90:
    print("Grade:B")
elif 70 <= grade < 80:
    print("Grade:C")
else:
    print("Below C")


# In[7]:


# Example 4: Nested if statement
num = 25

if num > 0:
    if num % 2 == 0:
        print("num is a positive even number.")
    else:
        print("num is a positive odd number.")
else:
    print("num is not a positive number.")


# In[8]:


# Example 5: Ternary operator
age = 21

status = "Adult" if age >= 18 else "Minor"
print(f"The person is a {status}.")


# In[ ]:





# In[ ]:





# In[ ]:




