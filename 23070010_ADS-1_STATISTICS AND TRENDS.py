#!/usr/bin/env python
# coding: utf-8

# In[43]:


#import all the required libraries

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#load the data set

salaries = pd.read_csv('C:/Users/mohan/Downloads/data_salaries/ds_salaries.csv')

print(df.head())


# In[23]:


# Display summary statistics of the dataset
print("Summary Statistics:")
print(salaries.describe())

# Display correlation matrix
print("\nCorrelation Matrix:")
print(salaries.corr())


# In[24]:


#plot the histogram for the above dataset

def plot_hist(salaries):
    
#plotting the bar chart for the dataset
    plt.bar(salaries['work_year'], salaries['salary_in_usd'], color = 'orange')
    
#add labels to the chart
    plt.xlabel('work_year', color = 'green')
    plt.ylabel('salary_in_usd', color = 'blue')
    
#modifying the x axis
    plt.xticks(rotation = 36)
    
#add title to the chart
    plt.title('Salaries', color = 'red')
    plt.grid(axis = 'y', linestyle = '--', alpha = 0.5)
    plt.show()
    


# In[25]:


plot_hist(salaries)


# In[36]:


#plot the scatter plot for the dataset
def plot_scatter(salaries):
    
    plt.scatter(salaries['work_year'], salaries['salary_in_usd'], color = 'violet', alpha = 0.5)
#add labels to the plot
    plt.xlabel('work_year', color = 'green')
    plt.ylabel('salary_in_usd', color = 'blue')
    plt.xticks(rotation = 36)
#add title to the plot
    plt.title('Salaries', color = 'red')
    plt.grid(True)
    plt.show()


# In[37]:


plot_scatter(salaries)


# In[44]:


#plot the heatmap for the dataset
def plot_heatmap(salaries):
    corr_matrix = salaries.select_dtypes(include='number').corr()
    sns.heatmap(corr_matrix,annot = True, fmt = '.2f', cmap = 'coolwarm', square = 'True')
# add title to the heatmap
    plt.title('Salaries', color = 'red')
    plt.show()
    


# In[45]:


plot_heatmap(salaries)


# In[ ]:




