# Day 35 --> Abstraction

#to have abstraction --> ABC class
#Managemetn system using OOP --> Assignment

#Method Overriding --> This happens when the child and the parent class possess the same method name but we want to have different behaviours.

#Hotstar scenario --> Free User (can watch limited content with advertisement)
#                 --> Paid User(can watch premium content without advertisement)
#                 --> Premium User(Watch live content without advertisement)
'''
class User:
    """Method overriding scenario"""
    def watch(self):
        print(f"can access basic content with advertisement")

class PaidUser(User):
    def watch(self):
        print(f'Can access premium content without advertisements')
    def paid_watch(self):
        print("can access premium content and basic content without advertisements")

u1 = User() #instance of User class can only access watch method from User class
u1.watch()
u2 = PaidUser() #instance of PaidUser class can access watch method from PaidUser class
u2.watch()
u2.paid_watch()
User.watch(u2)
'''

#Different subscriptions plans
'''
class free_User:
    """Method overriding with Hotstar scenario of different subscriptions plans"""
    def watch(self):
        print(f"watching free content with advertisements")

class vip_User(free_User):
    def watch(self):
        print(f"watching premium content without advertisements")
        super().watch()

class Premium_User(vip_User):
    def watch(self):
        print(f'Watching live content and premium movies')
        super().watch()

u1 = free_User()
u1.watch()
u2 = vip_User()
u2.watch()
u3 = Premium_User()
u3.watch()
'''

#Operator Overloading --> 
#__add__ --> Python special method / magic methods / dunder methods
#__str__,__init__
'''
a = "15"; b = "25"
print(a + b) #returns 40 because the operands are integers
print(a.__add__(b)) #this also returns 40
#if a and b are strings then __add__ or + treats them differenty
#when the opreands are int then the addition adds the numbers arithmetically
#if operands are strings then the addition concatenates them

c = 24
print(c.__mul__(4))
print(dir(c))
'''

#WatchHistory in Hotstar scenario
'''
class WatchHistory:
    """Understanding operator overloadin"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours

user1 = WatchHistory(120)
print(user1.hours)
user2 = WatchHistory(100)
print(user2.hours)
print(user1 + user2)
print(user1.__str__())
print(user2.__str__())


#when we want to use a operator between two objects, we should define the dunder method of that operator like
# __add__ for + etc, so when you apply + between two class instances of same class, the __add__ in the class gets calles\
#the dunder method definitions in the class can be overriden as per requirement
'''

#Abstraction --> it is the process of hiding unnexessary and only showing required data
#use only with abc module (abstractmethod)
#Instagram --> Upload photo, post reel, comment, etc

from abc import ABC,abstractmethod

class Content():
    #@abstractmethod
    def upload(self):
        pass

class photo(Content):
    def upload(self):
        print("Uploading photo")

class video(Content):
    def upload(self):
        print("Uploading video")

class reel(Content):
    def upload(self):
        print("Uploading Reel")

contents = [photo(),video(),reel()]
for content in contents:
    content.upload()