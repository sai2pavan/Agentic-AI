# Day 33 --> inheritence , super() method

'''
syntax:

class Parent:
    pass
class child(Parent):
    pass
class child2(Parent):
    pass
'''
'''
class RBI:
    """Parent class with major cash holding"""
    cash = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        print(f'RBI has {cls.available_cash} Rupees as cash')

class SBI(RBI):
    pass

class HDFC(RBI):
    cash = 5000000

    @classmethod
    def hdfc_cash(cls):
        
        print(f'HDFC cash is {HDFC.cash}')
        print(f'Total Cash accessible for HDFC is {RBI.cash + HDFC.cash}')

a = HDFC()
a.hdfc_cash()
'''

#Father --> Kid Property
#In this case we will have constructor only in parent class
'''
class Father:
    """Father class will have some property"""
    property = 5000000
    def __init__(self):
        self.property = 5000000
    def father_property(self):
        print(f'father property value is {self.property}')

class kid(Father):
    def __init__(self):
        self.property = 100000
    def kid_property(self):
        print(f'kid own property is {self.property}')
        print(f'kid final property is {self.property + self.property}')

value = kid()
print(value.property)
value.father_property()
value.kid_property()
#this is printing the value but not as intended, it is considering only the kids value
'''
'''
class Father:
    """Father class will have some property"""
    property = 5000000
    def __init__(self):
        self.property = 5000000
    def father_property(self):
        print(f'father property value is {self.property}')

class kid(Father):
    def __init__(self):
        self.property1 = 100000
    def kid_property(self):
        print(f'kid own property is {self.property1}')
        print(f'kid final property is {self.property + self.property1}')
#the constructor present in the father class is being overridden by constructor in kid class
value = kid()
print(value.property1)
value.father_property()
value.kid_property()
'''
'''
#to handle constructor overriding we use the super() method
super().__init__() #class superclass constructor
super().__init__() #calls superclass constructor with arguments
super().method() #calls superclass method
'''
'''
class Father:
    """Father class will have some property"""
    def __init__(self,property):
        self.property = property
    def father_property(self):
        print(f'father property value is {self.property}')

class kid(Father):
    def __init__(self,property,property1):
        self.property1 = property1
        super().__init__(property)
    def kid_property(self):
        print(f'kid own property is {self.property1}')
        print(f'kid final property is {self.property + self.property1}')

value = kid(5000000,100000)
print(value.property)
(value.property1)
value.kid_property()
'''
'''
#Area Calculation scenario
#we use supermethod() when we have a method in both the class with same name
#we use super method to access the method from parent
class Square:
    """square area calculation with constructor"""
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f'Area of square is {self.x * self.x}')

class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    def area(self):
        super().area()
        print(f'Area of rectangle is {self.x * self.y}')

result = Rectangle(4,5)
result.area()
'''

#Multiple inheritencee --> one child class acquiring properties from multiple parent class
'''
syntax:
class baseclass_1:
    pass
class baseclass_2:
    pass
class derived_class(baseclass_1,baseclass_2):
    pass
'''
'''
class Users:
    """Users with simple feature"""
    def send_message(self):
        print('Sending message')

class Notification:
    """Sending notification"""
    def notification(self):
        print("Notification sent")

class PremiumUsers(Users,Notification):
    """Premium users"""
    def premium(self):
        print("Accessing Premium Features")

user1 = PremiumUsers()
print(dir(user1))
user1.premium()
user1.notification()
user1.send_message()
'''

#Multilevel inheritence --> one class acquiring properties from another
'''
class GrandParent:
    pass
class Parent(GrandParent):
    pass
class Child(Parent):
    pass
'''

class Users:
    def make_calls(self):
        print("Making calls")

class Business_Users(Users):
    def create_catalog(self):
        print("Can Create Catalog")

class Verified_Business_Users(Business_Users):
    def blue_tick(self):
        print("gets blue tick")


