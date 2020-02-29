#!/usr/bin/env python
# coding: utf-8

# In[2]:


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        unprinted_design = unprinted_designs.pop()
        print('Printing model: ' + unprinted_design)
        completed_models.append(unprinted_design)
        
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)
        


# In[ ]:




