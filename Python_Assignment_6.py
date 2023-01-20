#!/usr/bin/env python
# coding: utf-8

# # PYTHON ASSIGNMENT - 6

# What are escape characters, and how do you use them?
# In Python strings, the backslash "" is a special character, 
# also called the "escape" character.
# It is used in representing certain whitespace characters:
# "\t" is a tab, "\n" is a newline, and "\r" is a carriage return
# 
# 

# In[15]:


print("my name is")


# 2.What do the escape characters n and t stand for?
# "\t" is a tab, "\n" is a newline

# 3.What is the way to include backslash characters in a string?

# In[16]:



print('its a back slash \ in a line')


# 4.The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
# The single quote in Howl's is fine because you've used double quotes to mark the beginning and end of the string. like wise we can use double quotes in with single quotes

# In[17]:


print("HowI's Moving Castle")


# In[18]:


# like wise we can use double quote in side single quote
print('Its a "Nice" Day')


# 5.How do you write a string of newlines if you don't want to use the n character?

# In[19]:


print("printing something in new line",end = '\n')
print("newline")


# 6.What are the values of the given expressions?
# 'Hello, world!'[1] 'Hello, world!'[0:5] 'Hello, world!'[:5] 'Hello, world!'[3:]
# 
# 

# In[22]:


'Hello, world!'[1]


# In[24]:


'Hello, world!'[0:5]


# In[25]:



'Hello, world!'[3:]


# 7.What are the values of the following expressions?
# 'Hello'.upper() 'Hello'.upper().isupper() 'Hello'.upper().lower()

# In[27]:


'Hello'.upper()


# In[28]:


'Hello'.upper().isupper()


# In[29]:


'Hello'.upper().lower()


# 8.What are the values of the following expressions?
# 'Remember, remember, the fifth of July.'.split() '-'.join('There can only one.'.split())

# In[30]:


'Remember, remember, the fifth of July.'.split()


# In[31]:


'-'.join('There can only one.'.split())


# 9.What are the methods for right-justifying, left-justifying, and centering a string?

# In[32]:


# left justified
str ="Shiva"
str.ljust(10,"-")


# In[33]:


# right justified
str ="My name is"
str.rjust(40,'*')


# In[34]:


# center justified
str ="My name is"
str.center(40,'*')
     


# In[35]:


str ="  gfgfgfgfgfgfgf yuyuyuuyuy  "
str.lstrip()


# In[36]:


str ="  yytytytyyt mmamamam  "
str.rstrip()


# In[ ]:




