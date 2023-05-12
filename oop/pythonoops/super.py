# Method overriding  
## if there is the  two method same 
# in child and parent class 
# Then  the child class run first
# which  is method overriding 




# use of super keyword


class Phone:
    def __init__(self,price,brand,camera):
        print("inside")
        self.__price = price 
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("buying")
class SmartPhone(Phone):
    def buy(self):
        print ("buying smart phone")
        super().buy() #syntax to call parent method
        
s = SmartPhone(20000,"mi",48)
s.buy()

# super is the  way to access the parent method if there
#  

# if both have constructor and we need to access the 
# method of parent {whenever we need then } 
# we use super keyword to access the parent method 
# If child and parent have both consists of contrutor
# then at child constructor  is claled 
# but  super is the way to access both constructor and  
# method of parent class 

 
 
 ##Super keyword is the smartest way to call
 # the both child and parent constructor 
 # if there  are no super keyword only one constructor 
 # are being called at a time 
 # if there is constructor in both without useing 
 # super keyword we cannot call the both
 # constructor 
 # if we have suuper keyword  we can call both constrcor 
 
 #=======================================================================
 #Summary of Super keyword
 # Superkeyword is not used inside parent and outside class
 # Super is used only inside the child class 
 # super keyword wont access the variable 
 #========================================================
 