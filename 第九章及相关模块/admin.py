#!/usr/bin/env python
# coding: utf-8

# In[1]:


from user import User

class Admin(User):
    '''a unique Adminstrator class'''
    def __init__(self,first_name, last_name, username, email,location):
        '''
        initialize the parent User Class
        initilize the unique Admin class
        '''
        super().__init__(first_name, last_name, username, email,location)
        self.privileges = Privileges()
        
        
class Privileges():
    '''a class to describe privileges'''
    def __init__(self):
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user'
        ]
    def show_privileges(self):
        '''a method to show privileges'''
        for privilege in self.privileges:
            print(' ' + privilege)


# In[ ]:




