# static method ==>>There can be some functionality that relates to the class, 
# but does not require any instance(s) to do some work, static methods can be 
# used in such cases. A static method is a method which is bound to the class and 
# not the object of the class. It can’t access or modify class state. 
# It is present in  a class because it makes sens for the method to be
#  present in class.A static method does not receive an implicit first argument.

##static method are memory efficient 
#The reason to use staticmethod is if you have
#  something that could be written as a standalone
#  function (not part of any class), but you want to
#  keep it within the class because it's somehow 
# semantically related to the class. (For instance, 
# it could be a function that doesn't require any 
# information from the class, but whose behavior is 
# specific to the class, so that subclasses might want 
# to override it.) In many cases, it could make just as
#  much sense to write somethingas a standalone function
#  instead of a staticmethod.
#==========================================================================================
''' 
Advantages of a Static Method
==============================
1)) Here, the static method has the following advantages

Consume Less memory: Instance methods are object too, and creating them has a cost. Having a static method
avoids that. Let’s assume you have ten employee objects and if you create gather_requirement() as a instance method then Python 
have to create a ten copies of this method (seperate for each object) which will consume more memeory. 
On the other hand static method has only one copy per class.
+==========================================================================================================
2) 
To Write Utility functions: Static methods have limited use because they don’t have access to the attributes of an object 
(instance variables) and class attributes (class variables). However, they can be helpful in utility such as conversion 
form one type to another. The parameters provided are enough to operate.Readabiltity: Seeing the @staticmethod at the top of
 the method, we know that the method does not depend on the object’s state or the class state.

'''


str = "shady"
#print(str.len())
for i,value in enumerate(str):
    print(i,value)

