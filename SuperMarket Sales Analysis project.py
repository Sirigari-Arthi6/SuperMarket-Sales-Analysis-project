#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset)


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.head(5))


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.tail(5))


# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.shape)


# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.info())


# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.isnull().sum())


# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.describe())


# In[16]:


# 1. which category has the highest sales?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")

dataset.groupby('Category')['Sales'].sum().sort_values(ascending=False).plot(kind='bar',title='Category-wise Sales')
plt.show()


# In[20]:


# 2. Which sub-category generates the most profit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10).plot(kind='bar',title='Top Profits From Sub-category'))


# In[21]:


# 3. Region-wise sales Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.groupby('Region')['Sales'].sum().plot(kind='pie',autopct='%1.1f%%',title='Region-wise sales Distribution'))


# In[32]:


# 4. Year-wise sales trend
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")

dataset['Order Date'] = pd.to_datetime(dataset['Order Date'])
dataset['Year']=dataset['Order Date'].dt.year

dataset.groupby('Year')['Sales'].sum().plot(kind='line',marker='o',title='Year-wise Sales trend')
plt.show()


# In[33]:


# 5. Customer Segment Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset.groupby('Segment')['Sales'].sum().sort_values(ascending=False).head(10).plot(kind='bar',title='Sales by Customer Segment'))


# In[38]:


# 6. Top 10 Product by sales
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("supermarket.csv")
print(dataset.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10))


# In[39]:


# 7. Ship Mode Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("supermarket.csv")
print(dataset['Ship Mode'].value_counts().plot(kind='pie',title='Ship Mode Distribution'))


# In[ ]:




