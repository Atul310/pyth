'''
Basically, Abstraction focuses on hiding the internal 
implementations of a process or method from the user. 
In this way, the user knows what he is doing but not
how the work is being done.

For example, people do not think of a car as a set of 
thousands of individual parts. Instead they see it as a 
well-defined object with its own unique behavior. This 
abstraction allows people to use a car to drive without 
knowing the complexity of the parts that form the car. 
They can ignore the details of how the engine 
transmission, and braking systems work. Instead, they 
are free to utilize the object as a whole.
A powerful way to manage abstraction is through the use 
of hierarchical classification. This allows us to layer 
the semantics of complex systems, breaking them into 
more manageable pieces. From the outside, a car is a 
single object. Once inside, you see that the car 
consists of several subsystems: steering, brakes, sound 
system, seat belts, etc. In turn, each of these 
subsystems is made up of smaller units.

The point is that we manage the complexity of the car (or any other complex system) through the use of hierarchical abstractions.


===========================================

abc module ==>> This module provides the infrastructure 
for defining abstract base classes (ABCs) in Python, as 
outlined in PEP 3119; see the PEP for why this was added 
to Python. (See also PEP 3141 and the numbers module 
regarding a type hierarchy for numbers based on ABCs.)


Abstract base classes ==>> 
'''
##abstract method doesnot have any implememttation
#ABC is the base class
from  abc import ABC,abstractmethod
class BankApp(ABC):
    def Database(self):
        print ("connected")
        
    @abstractmethod
    def security(): ## this is abstract metod
        pass
class MobileApp(BankApp):
    def mobile_login(self): 
        print("login to mob")
    def security(): #this method should be implemented to 
        pass         # acess and make the object of mobileapp
a = MobileApp()
(a.mobile_login())

## to access the abstract class we need to speci