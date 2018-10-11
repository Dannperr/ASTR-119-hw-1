#!/usr/bin/env python
# coding: utf-8

# In[1]:


example_dict = {
    'class' : 'ASTR 119',
    'prof'  : 'Brant',
    'awesomeness' : 10
}


# In[2]:


print(type(example_dict)) # will say dict


# In[3]:


#get a value via key
course = example_dict['class']
print(course)


# In[4]:


#change a value via key
example_dict['awesomeness'] += 1 #increase awesomeness


# In[5]:


#print the dictionary
print(example_dict)


# In[6]:


#print dictionary element by element
for x in example_dict.keys():
    print(x,example_dict[x])


# In[ ]:




