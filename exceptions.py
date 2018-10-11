#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python exceptions let you deal with
#unexpected results

try:
    print(a)    # this will throw an exception since a is not defined
except:
    print('a is not defined!')


# In[3]:


#there are specific errors to help with cases

try:
    print(a) # this will throw an exception since a is not defined
except NameError:
    print('a is still not defined!')
except:
    print('Something else went wrong.')


# In[5]:


#this will break our program
#since a is not defined
print(a)

