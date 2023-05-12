##mutability of object +=>> chage without creating new
#things  
# object are  by default mutable 

#Encapusalation  ==>Encapsulation is the packing 
# of data and functions that work on that data within 
# a single object. By doing so, you can hide the 
# internal state of the object 
# from the outside. This is known as information hiding.
#


##

##  if  we put __(double under score) to a variable and 
# method in python it becomes the {private } attriubute(variable)
#and  method

# When we creatae a provate variable 
# then in memory our variable changes  to 
# suppose the variable name = __VariableName
#_className__variableName 

# in python nothing is truly Private  inside class 
# we  can change private  varibale and method from outside 
#the class
# by private method and variable we can hide data 
# but the data can be excessed outside the class 
# even though the variable and method are  private

# getter and setter method helps to show and change the
# private variable and method

## Make variable and method private as much as possible
## 

class ATM:
    def __init__(self):
        self.__pin ="" # this became private  by __
        self.__balance =0
        self.menu()
        
    def menu(self):
       user_input = input("""
              Hi can  I help you ?
              1. press 1 to create pin 
              2. press 2 to chage the pin 
              3. check balance at 3
              4. 4 to withdraw 
              5 . 5 to exit 
              """)
       if user_input =="1":
           self.create_pin()
       elif user_input == "2":
           self.chage_pin()
       elif user_input=="3":
           self.check_balance()
    def create_pin(self):
        Usr_pn = input("enter pin")
        self.pin =Usr_pn
        usr_bal = input("enter balanec")
        self.__balance= usr_bal
        print("created pin")
        self.menu()
    def chage_pin(self):
        user_pin = input("enter the old pin ")
        if user_pin == self.pin:
            new_pin = input("enter new pin")
            self.pin = new_pin
            self.menu()
            
            
        else:
          print("incorrect pin try again !!!")
          self.menu()
    def check_balance(self):
        usr_pin =input("input pin")
        if self.pin == usr_pin:
            print(" your balance is :",self.balance)
        else:
            print("your pin is incorrect")
    def Withdraw(self):
        user_iinp =input("first enter pin")
        if user_iinp == self.pin:
            #print("enter the amount to withdraw")
            amount = int(input("enter ampunt"))
            if amount <= self.balance:
             slef.__balance= __balance-amount
             print("withdrawn successfull")
            else:
                print("try agatin")
            
            
        
        else:
            print("please correct your pin and try again")
        self.menu()       
a = ATM()
# a.__balance = # it doesntot work 
#because we cannot excess the private variable by 
# using the samme private  variable 
# the variable stores as _ATM__balance in the memory 
#location 


#use of getter and setter 
# we can give privelage to change the 
# private variable and method and set the variable and
#value throught the help of function
