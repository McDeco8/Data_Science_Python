#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Loop Control statement in Python


# In[4]:


# Example 1: For loop to iterate over a sequence
fruits = ["apple", "banana", "mango","grape","peach"]

for fruit in fruits:
    print(f"I like {fruit}s.")


# In[6]:


# Example 2: While loop to print numbers from 1 to 5
count = 1

while count <= 15:
    print(count)
    count += 1


# In[ ]:


# Example 3: Using break statement to exit a loop
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 4:
        break
    print(num)


# In[ ]:


# Example 4: Using continue statement to skip specific iterations
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)


# In[ ]:


# Example 5: For-else loop with a condition
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        break
else:
    print("Loop completed without encountering a break.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




