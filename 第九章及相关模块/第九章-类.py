#!/usr/bin/env python
# coding: utf-8

# In[6]:


# 9-1 餐馆
class Restaurant():
    '''a class representing a restaurant'''
    def __init__(self,restaurant_name, cuisine_type):
        '''initialize the restaurant'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        '''a method to describe the restaurant'''
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type)
        
    def open_restaurant(self):
        '''a method to describe open restaurant'''
        print(self.restaurant_name + ' now, is opening!!!')
        
restaurant = Restaurant('云海肴', '云南菜')
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


# In[8]:


# 9-2 略


# In[11]:


# 9-3 用户
class User():
    '''a class representing a User'''
    def __init__(self, first_name, last_name, username, email,location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email
        self.location = location
    
    def describe_user(self):
        '''a method to describe a user information'''
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
        
    def greet_user(self):
        '''a method to greet user'''
        print("\nWelcome back, " + self.username + "!")
            
user_1 = User('pengfei','chen','Eziogriggo','Eziogriggo@hotmail.com','kunming')
user_1.describe_user()
user_1.greet_user()


# In[24]:


# 9-4 就餐人数
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
        

restaurant = Restaurant('云海肴', '云南菜')
print('Number served in intital: ' + str(restaurant.number_served))

'''Change the inital vlue for number served to 200'''
restaurant.number_served = 200
print('Number served: ' + str(restaurant.number_served))

'''call number_served method inside the class'''
restaurant.set_number_served(150)
print('Number served: ' + str(restaurant.number_served))

'''call increment_number_served method inside the class'''
restaurant.increment_number_served(120)
print('After increase, the number served: ' + str(restaurant.number_served))


# In[32]:


#9-5 尝试登录次数
class User():
    '''a class representing a User'''
    def __init__(self, first_name, last_name, username, email,location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.title()
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        '''a method to describe a user information'''
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)
        
    def greet_user(self):
        '''a method to greet user'''
        print("\nWelcome back, " + self.username + "!")
        
    def increment_login_attempts(self):
        '''a method to increase login attempts'''
        self.login_attempts += 1
     
    def reset_login_attempts(self):
        '''a method to rest login attempts'''
        self.login_attempts = 0
        
            
user_1 = User('pengfei','chen','Eziogriggo','Eziogriggo@hotmail.com','kunming')
user_1.describe_user()
user_1.greet_user()

'''to call and increase user login attempts'''
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print('\nAccumulative login attempts: ' + str(user_1.login_attempts))

'''ret user login attempts '''
user_1.reset_login_attempts()
print('\nResetting the login attempts.....')
print('Accumulative login attempts: ' + str(user_1.login_attempts))


# In[35]:


# 9-6 冰淇淋小店
class Restaurant():
    '''a class representing a restaurant'''
    def __init__(self,restaurant_name, cuisine_type):
        '''initialize the restaurant'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        '''a method to describe the restaurant'''
        print(self.restaurant_name.title() + ' serves ' + self.cuisine_type)
        
    def set_number_served(self,number_served):
        '''a method to set up number served people'''
        self.number_served = number_served
        
    def increment_number_served(self, number_served):
        '''a method to increment the number served people'''
        self.number_served += number_served
        
class IceCreamStand(Restaurant):
    '''a ice cream store'''
    def __init__(self, restaurant_name, cuisine_type):
        '''Initialize the parent class member'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)
            
big_one = IceCreamStand('The Big One','Ice Cream')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

'''call show flavor in the class'''
big_one.describe_restaurant()
big_one.show_flavors()


# In[42]:


# 9-7 管理员
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

class Admin(User):
    '''a unique Adminstrator class'''
    def __init__(self,first_name, last_name, username, email,location):
        '''
        initialize the parent User Class
        initilize the unique Admin class
        '''
        super().__init__(first_name, last_name, username, email,location)
        self.privileges = []   
    def show_privileges(self):
        '''a method to show privileges'''
        for privilege in self.privileges:
            print(' ' + privilege)

admin_1 = Admin('xuemei','chen','pchen55','pchen55@jhu.edu','kunming')
admin_1.describe_user()


'''call the show privilege from admin class'''
print('\nThis is Administors with following privileges:')
admin_1.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

admin_1.show_privileges()


# In[46]:


# 9-8 权限
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
            
admin_1 = Admin('xuemei','chen','pchen55','pchen55@jhu.edu','kunming')
admin_1.describe_user()

'''call the show privilege from admin class'''
print('\nThis is Administors with following privileges:')
admin_1.privileges.show_privileges()


# In[50]:


# 9-9 电瓶升级
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrade_battery(self):
        '''a method to upgrade battery'''
        if self.battery_size != 85:
            self.battery_size = 85

        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''to upgrade battery'''
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


# In[3]:


# 9-13使用OrderedDict

from collections import OrderedDict
glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for value, key in glossary.items():
    print(key + ': ' + value)


# In[31]:


# 9-14 骰子
from random import randint
class Die():
    '''roll a dice'''
    def __init__(self,sides=6):
        self.sides = sides
        
    def roll_die(self):
        '''a function to roll die'''
        die_side = randint(1,self.sides)
        return die_side
    
    
die = Die()
results = []
for roll_number in range(10):
    result = die.roll_die()
    results.append(result)
    
print("10 rolls of a 6-sided die:")
print(results)


# In[ ]:




