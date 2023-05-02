#!/usr/bin/env python
# coding: utf-8

# ## Numpy:Package for multidimensional array

# In[1]:


import numpy as np


# In[2]:


simple_list=[6,7,9]
np.array(simple_list)


# In[4]:


arr=np.array([1,2,3])
arr


# In[5]:


list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
np.array(list_of_lists)


# In[6]:


np.arange(5,65)


# In[7]:


np.arange(1,30,2)


# In[8]:


np.zeros(10)


# In[9]:


np.zeros(10,int)


# In[10]:


np.ones(100)


# In[11]:


np.ones(100,int)


# In[17]:


np.ones((2,5),int)


# In[14]:


np.arange(0,51)


# In[15]:


np.arange(5,26,5)


# In[18]:


np.zeros((2,5),int)


# In[19]:


np.linspace(0,1,5)


# In[21]:


np.linspace(0,20,8)


# In[29]:


np.eye((10),dtype=int)


# In[32]:


np.random.rand(2,4)


# In[34]:


arr=np.random.randn(2,4)
arr


# In[35]:


np.random.randn(3,5)


# In[37]:


np.random.randint(2,10)


# In[38]:


np.random.rand(3,5)


# In[40]:


np.random.randint(20,56,100)


# In[41]:


sample_array=np.arange(30)
sample_array


# In[55]:


rand_array=np.random.randint(0,100,20)
rand_array


# In[84]:


sample_array.reshape(5,9)
# it throws error as 5x9=45 but we have only 30 samples in the array


# In[85]:


sample_array.max()


# In[86]:


rand_array.min()


# In[87]:


rand_array.max()


# In[88]:


rand_array.argmax()


# In[89]:


a=np.eye(5)
a
#identity matrix of 5x5


# In[90]:


a.T


# In[91]:


a=np.random.rand(2,3)
a


# In[92]:


a.T


# In[93]:


sample_array=np.arange(10,21)
sample_array


# In[94]:


sample_array[8]


# In[95]:


sample_array[2:5]


# In[96]:


sample_array[1:4]=100
sample_array


# In[97]:


subset_sample_array=sample_array[0:7]
subset_sample_array


# In[98]:


sample_array[0:7]


# In[99]:


subset_sample_array[:]=1001
subset_sample_array


# ## Two-Dimensional array

# In[100]:


import numpy as np


# In[101]:


sample_matrix=np.array(([50,20,2,34],[43,23,20,33],[56,76,22,7]))
sample_matrix


# In[102]:


sample_matrix[0][2]


# In[108]:


sample_matrix[1,2]


# In[109]:


sample_matrix[:,(3,2)]


# ## Selection Technique

# In[110]:


sample_array=np.arange(1,25)
sample_array


# In[111]:


sample_array+sample_array


# In[113]:


np.exp(sample_array) #exponential


# In[114]:


np.sqrt(sample_array)


# In[115]:


np.log(sample_array)


# In[116]:


np.max(sample_array)


# In[117]:


np.min(sample_array)


# In[118]:


np.argmax(sample_array)


# In[119]:


np.argmin(sample_array)


# In[120]:


np.square(sample_array)


# In[121]:


np.std(sample_array)


# In[122]:


np.var(sample_array)


# In[123]:


np.mean(sample_array)


# In[125]:


array=np.random.randn(3,4)
array


# In[126]:


np.round(array,decimals=2)


# In[131]:


sports=np.array(['golf','cricket','fball','cricket'])
np.unique(sports)


# ## PANDAS

# In[133]:


import pandas as pd
import numpy as np


# In[ ]:




