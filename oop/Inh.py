#inheritance ==>> it is the real workd concept extracted 
#It is a feature that enables a class to acquire 
# properties and characteristics of another class.
#

#Inheritance provides code reusaibility 

# for example there look at the below coe 

class User: #this is parent class
    def __init__(self):
        self.__name="Atul"
# the above is private variable we cannot access it directly
#we can access it by getter method 
# if parent class gives getter method  to get the value
        #slef.name="Atul"
        self.gender= "male"
    def get_name(self):
        print(self.__name)
    
class student (User):# student class is child class
  def login(self):
        print("login")
  

s = student()
print(s.get_name())
print(s.gender)
''' 
Here we have passed (User) to the class 
student so here 
student class cann acess the all attribute and method 
of User class 


here ==>> User is the parent class 
and student is the child class 

==>> inheritance is happednd here 

child class can iherit the parent clas

# in some scenario child class can be parent also 

'''


if __name__ =="main":
    print(main)


#concept no 1 
# if child doesnot have its own constructor 
# parent constructor is called 
#
# IF child has its own constructor 
# then parent constructor is not called 
# the value inside parent constructor is not inatalized
# if the value are not inatilized ()
# the child class cannot access the parent variable ,methods
# because they are not inatilized (they are not formed)
#==============================================

## We cannot access the private members of 
# Parent class by child class 

