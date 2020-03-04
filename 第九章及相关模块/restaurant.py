#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Restaurant():
    '''a class representing a restaurant'''
    def __init__(self,restaurant_name, cuisine_type):
        '''initialize the restaurant'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def set_number_served(self,number_served):
        '''a method to set up number served people'''
        self.number_served = number_served
        
    def increment_number_served(self, number_served):
        '''a method to increment the number served people'''
        self.number_served += number_served

