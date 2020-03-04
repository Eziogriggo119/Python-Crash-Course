#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class User():
    '''a class representing a User'''
    def __init__(self, first_name, last_name, username, email,location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email
        self.location = location.title()
    
    def describe_user(self):
        '''a method to describe a user information'''
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
        
        

