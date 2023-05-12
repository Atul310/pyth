# super wnd example 

class Phone:
    def __init__(self,price,brand,camera):
        print("inside Parent constructor ")
        self.__price = price 
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("buying")
class SmartPhone(Phone):
    def __init__(self, price, brand, camera,os,ram):
        super().__init__(price, brand, camera)
        print("inside smartphone constr ")
        self.os = os 
        self.ram= ram
        print("inside smartphone ")
   # def buy(self):
        #print ("buying smart phone")
        #super().buy() #syntax to call parent method
        
        
s = SmartPhone(20000,"mi",48,"miui","4gb")
#s.buy()
'''
Output of above code ==>>

================================================

 └──╼ $python3 super2.py
inside Parent constructor 
inside smartphone constr 
inside smartphone 
===================================================


Here above  by using super keyword we have used both the 
constructor inside parent and child class 


'''