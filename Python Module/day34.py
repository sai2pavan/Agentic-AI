# Day 34 --> Hierarchical inheritance, Hybrid inheritence, Polymorphism

#hierarchical inheritance --> Type of inheritence where multiple child classes inherit properties from single parent (base) class
'''
Syntax:
class Parent:
    pass
class child(Parent):
    pass
class child2(Parent):
    pass
class child3(Parent):
    pass
class child4(Parent):
    pass
'''

#whatsapp Scenario
'''
class User:
    """User class with message properties"""
    def send_message(self):
        print(f"sending message")

class PersonalUser(User):
    """Personal User class inheriting from user class"""
    def status_update(self):
        print(f'status updated only for contacts')

class BusinessUser(User):
    """Business User can also create catalogs"""
    def create_catalog(self):
        print(f'catalog creation is possible')

class VerifiedBusinessUser(User):
    """Verified User"""
    def premium_user(self):
        print(f"blue tick added and premium features loaded")

class CommunityAdmin(User):
    """Community admin access"""
    def create_community(self):
        print(f"access to community operations")


user1 = User()
user1.send_message()
user2 = PersonalUser()
user2.send_message()
user2.status_update()
user3 = BusinessUser()
user3.send_message()
user3.create_catalog()
user4 = VerifiedBusinessUser()
user4.send_message()
user4.premium_user()
user5 = CommunityAdmin()
user5.send_message()
user5.create_community()
'''

#Hybrid inheritence --> it is a type of inheritence in which one or more than one type of inheritences can be applicable
'''
class User:
    """User class with voice calls"""
    def voice_call(self):
        print(f"making voice call")
    def video_call(self):
        print(f"making video call")

class Notification(User):
    """Sending Notification"""
    def notify(self):
        print("Sending Notification")

class BusinessUser:
    """Business user access"""
    def create_catalog(self):
        print("can create business catalog")

class PremiumBusinessUser(BusinessUser,Notification):
    """Premium features accessible"""
    def premium_access(self):
        print(f'blue tick verification and reach access')

u1 = BusinessUser()
u1.create_catalog()
u2 = PremiumBusinessUser()
u2.voice_call()
u2.video_call()
u2.notify()
u2.create_catalog()
u2.premium_access()
'''

#Polymorphism --> feature of OOP
#Poly --> many
#morph --> forms
'''
Method Overloading
Method overriding
Operator Overloading --> __add__,__str__

#hotstar --> freeuser,premium,user, adv, premium user
'''
'''
class Hotstar:
    """Simple example to understand polymorphism"""
    def watch(self):
        print(f"welcome to hotstar")
    def watch(self,movie):
        self.movie = movie
        print(f'loaded hotstar Playing {self.movie}')



user = Hotstar()
user.watch('spiderman')
user.watch()
'''
'''
#Method overloading with default arguments
class Hotstar:
    """Method overloading with default arguments"""
    watchlist = []
    def watch(self,movie):
        if movie == None:
            print('Welcome to hotstar')
        else:
            print(f"playing {movie}")
    @classmethod
    def add_to_watchlist(self,*movies):
        


#user = Hotstar()
#user.add_to_watchlist
'''