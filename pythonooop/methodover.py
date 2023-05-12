'''

Method overriding is an ability of any object-oriented 
programming language 
that allows  child class to 
provide a specific implementation of a method that is 
already provided by one of its super-classes or parent classes 

'''


## The concept of method overriding is simple as it is 
# if There is inheritance in a class
# And  child class and parent class has
# same method .Then the method of child is always 
#executed not the parent method 
# It is similar to constructor over riding 
# since constructor is also method it is called
#as method overriding
# IF child has its own constructor then the first 
#child constructor is called 
# and if child class doesnot have its own constructor 
# then parent constructor is called 

# if both have constructor then the child constructor is called

class Phone: 
    def __init__(self,price,name):
        print("inside cons")
        self.price= price
        self.name=name
        
    def buy(self):
        print("buy")
    
class Smartphone(Phone):
    def buy(self):
        print("this is smartphone")
    
s = Smartphone(200, "name")
s.buy()
# output is  
''' 
└──╼ $python3 methodover.py
inside cons ==>>> this is of constructor
this is smartphone => this is the method 



'''
sa = Phone(20, "name")
sa.buy()
# this call the parent calss method as it is individual 



## The use of SuperKeyword

