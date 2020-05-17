#!/usr/bin/env python
# coding: utf-8

# In[4]:



from IPython.display import IFrame
IFrame('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', width=300, height=200)


# In[ ]:


# import load_iris function from datasets module
from sklearn.datasets import load_iris


# In[5]:


# save "bunch" object containing iris dataset and its attributes
iris = load_iris()
type(iris)


# In[6]:


# print the iris data
print(iris.data)


# In[7]:


# print the names of the four features
print(iris.feature_names)


# In[8]:


# print integers representing the species of each observation
print(iris.target)


# In[9]:


# print the encoding scheme for species: 0 = setosa, 1 = versicolor, 2 = virginica
print(iris.target_names)


# In[10]:


# check the types of the features and response
print(type(iris.data))
print(type(iris.target))


# In[11]:


# check the shape of the features (first dimension = number of observations, second dimensions = number of features)
print(iris.data.shape)


# In[12]:


# check the shape of the response (single dimension matching the number of observations)
print(iris.target.shape)


# In[13]:


# store feature matrix in "X"
X = iris.data

# store response vector in "y"
y = iris.target


# In[ ]:




