#!/usr/bin/env python
# coding: utf-8

# # perform arithmetic operations (+, -, *,/, and %).

# In[1]:


import pandas as pd
user=list(map(int,input().split()))
df=pd.Series(user)
print("sample input is",*df)
result=[]
for i in df:
    a = (i**2)
    result.append(a)
print("sample output is ",*result)


# ## 5 inputs and then it will display the power of all those inputs, taken in the first series. 

# # Method 1

# In[2]:


import pandas as pd
user1=list(map(int,input().split()))
user2=list(map(int,input().split()))
ds1 = pd.Series(user1)
ds2 = pd.Series(user2)
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)


# # METHOD 2

# In[11]:



import pandas as pd
user1=list(map(int,input().split()))
user2=list(map(int,input().split()))
s1=pd.Series(user1)
#print(s1)
#print(s2)
s2=pd.Series(user1)
def add(s1,s2):
    
    print("add two series",s1+s2,end=" ")
def sub(a,b):
    print("subs two series",s1-s2,end=" ")
def product(a,b):
    print("product of two series",s1*s2,end=" ")
def divide(a,b):
    print("division of two series",s1/s2,end=" ") 
print(add(s1,s2))
print(sub(s1,s2))
print(product(s1,s2))
print(divide(s1,s2))
    


# In[ ]:




