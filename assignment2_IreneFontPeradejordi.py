
# coding: utf-8

# In[14]:


def multi3_odd(start, finish):
    total = 0
    for x in range(start, finish):
        if (x%3 == 0) and (x%2 != 0):
            total += 1
    return total


# In[15]:


multi3_odd(3,12)


# In[17]:


multi3_odd(3,200)

