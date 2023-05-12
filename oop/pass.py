class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
        
def greet(person): # parameter 
    #This is the function and we have given the refrence
    #of object to function known as pass by refrence
    print("ame",person.name,"age",person.age)
   
p = Person ("Atl", 22)

greet(p) # this is paramater is passsed 
# p is the object refrence     and this is arument 
 
 # p object goes to person parameter  and 
 # pront the name and age 
 

 # object are mutable that means we can change the value of object once creat e
 
 
 
 