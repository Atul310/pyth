# We can access the private attribute and method by 
#getter metho
class Parent:
    def __init__(self,num):
        self.__num = num
    def get_num(self):
        return self.__num
class child(Parent):
    #def show(self):
        print("this is child class")
    
son = child(100)
print(son.get_num())
#son.show()

''' 

# At first we inherit the parent class in by child class

# there is private variable __num in the Parent class 
# which we neeed to access by the child class 
# as we know we cannot directly access the private method 
# we nedd gettter  method
getter method will help to get the private attribute 
so we define
get_num() as getter method 
which will return private member 
as in above 
return self.__num

In child class there is inhertance done
class child(parent):
    def show(self)
#here child doesnot have its own constructor 
# so parent constructor is called 
when we make object of child class 
son = child(100)
# the 100 is stored in self.__num = num variable 
#
and when we call 
son.get_num() ==>> this act as getter method 
the stored value of private variable get printed  
in console


'''