# thhe use of 
#__init__() method  
# consustructor is used to write configuration code 
# just like database connection code , internet connection code
# constructor method code is not given privelage  to use by
#users(custormer
# )
#constructor load automatically 
# if we give the constructor code to the user it is the flexible

# use of self keyword

#we can only access the methods and function inside
#our class using object only 
# dirctly communicating with the method betwee the classes
#is not possible
#=============================

#so we use self to make communicaticate between the 
#method inside the class
#=========================================

## we cannot call the method by another method inside sae 
#also

# self is the object refrecnce 
class Animal :
    name = "at"
    def __init__(self):
        self.name= ""
    
ab = Animal()



class Person:
    def __init__(self,name,age):
        self.name = nam
        self.age =ag



def greet(Person):
    pass
    
p = Person("Atul", 21)
greet(p)
