#!/usr/bin/env python
# coding: utf-8

# # PYTHON ASSIGNMENT 5

# 1.What does an empty dictionary's code look like?

# In[1]:


dict={}
type(dict)


# 2.What is the value of a dictionary value with the key 'foo' and the value 42?

# In[2]:


{'foo':42}


# 3.What is the most significant distinction between a dictionary and a list?
# Most significant difference:
# List - items in list are Ordered
# Dictionary : iten in dictionary are unordered

# 4.What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# In[3]:


spam = {'bar':100}
spam['foo']
#This will give us key error


# 5.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

# In[4]:


spam ={'cat':100}
'cat' in spam


# In[5]:


'cat' in spam.keys()
#There is no differnce, both check if 'cat' is key of the dictionary and if its a key, returns True.


# 6.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

# In[8]:


spam ={'cat':100}
'cat' in spam


# In[9]:


spam ={'cat':100}
'cat' in spam.values()

#'cat' in spam checks whether there is a 'cat' key in the dictionary
#'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# 7.What is a shortcut for the following code?

# In[10]:



spam ={'cat':100}
spam.setdefault('color','black')
spam


# 8.How do you 'pretty print' dictionary values using which module and function?

# In[11]:


import pprint
dct = [ {'Name': 'Shiva', 'Age': '23', 'Country': 'India'},
  {'Name': 'Anna', 'Age': '44', 'Country': 'China'},
  {'Name': 'Joe', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Chumlee', 'Age': '35', 'Country': 'USA'}
]


# In[12]:


# printing with pprint()
pprint.pprint(dct)
     
    


# In[14]:


#Printing with print()
print(dct)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




