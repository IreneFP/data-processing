
# coding: utf-8

# # Assignment 1

# Write a function days_in_seconds that takes a number days, and returns a string with the format 'X days = Y seconds', where X is equal to the value in the parameter days and Y is equal to the number of seconds in X days:
# 
# def days_in_seconds(days):
# 
#         #fill in the body of the function and return the appropriate value.
# 
# For example, days_in_seconds(3) returns '3 days = 4320 seconds'. 
# 
# Note that:
# 
# You can assume that days is a positive integer.
# You must follow the formatting carefully: all letters in the returned string must be lower-cased, and there should be a exactly one space between words and punctuation marks. There are no extra spaces at the beginning and at the end of the returned string.

# In[40]:


def days_in_seconds(days):
    days_seconds = days * 24 * 60 * 60
    answer = str(days) + " days = " + str(days_seconds) + " seconds"
    return answer


# In[43]:


days_in_seconds(3)


# In[42]:


days_in_seconds(1230)

