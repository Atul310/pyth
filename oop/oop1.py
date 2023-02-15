'''
Cl
ass 
object 
and Refrence variable 


class ==> Class are the blue print of the  object 

We can have one blue print and multiple object are  possible 



instance==>>
Object ===>> Physical exitstence of the blue print 

A instance of class is nothing but object

suppose We have a building to construct we first make the 
blue print and then we make the physical object 

With one class(blueprint) we can make multiple  physical 
things (i.e objects)




Refrence variable  ==>> variable used to refer the object

The main purose of refrence variable is to perform desired operation
on a particular object


For a partiular  object we have any number of refrence variable



Suppose we have  refrence variable but no object then 
such variable are not used so wwe throw it away 

garbage collection concept


'''


class Student:
    name = Atul
 



ab = Student()

print(ab.name)


#Static variable
#Static variable ==>>

##
""" 
        Use of Static variable ==>> If the value of the variable 
        doesnot change from object to object is called as static
        variable.

      #static variable  ==>>
         Static variable are directly declared inside class
      value of each  object is same if the varible is static 

     only one copy of variable is created and shared to 
     a     ll the objects of the same classes 

 
       ##
      # ===
       Static varaible are created  within the class directly
          but outside
        any method
        
  2)) Second way to create Static variable is 
  inside the constructor by using the class name 
  
  
  #)) Third way to create static variable is inside instance
  method by using class name .
  
  4)) 4TH WAY to create the static variable is 
  inside class method by using either cls or classnamee
  ======================================
  
  eg pf class method
class MyClass
  
  @classmethod 
  def m2(cls):
      cls.d=40
      MyClass.e=40
      
  
  
  
  ===============
  
  5) Fifth way to create static variable is by using 
  classname
 
  
  @static method
  
  
  
  
  
  6th method to create static variable is 
  
  ==>> outside of class by using class Name
  
  
  MyClass.Variable_name =20:
      
  
 
 
           Static variable are  called as class level variable 
         =====
 
 
 
 
Instance variable ==>> valuses of variable varies of object 
to object then it is called as instance variable 


Instance variable are object level variable 
seperate  copy ..


def __init__(self)


 """
    
  
  
      
      
        
        
        
        
 






