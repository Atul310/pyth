##instance method 

class Student:
    def study(self,oh): ##this method can only accessed 
        #by object of this class  
        self.hours=oh
        return self.hours

s1= Student()
print(s1.study(10))  ##calling method 
##s1 is the obj of class Student and study is method

#Instance Methods can also access and modify the
#  state/attributes of a class  by using the
#  self.__class__ attributue

class Student:
    
    no_of_students = 10

    def __init__(self, name, age):
       self.nama= name
       self.age = age

    def birthday(self):
       self.age += 1
       return f"{self.name} has now turned {self.age}\n" \
              f"{self.no_of_students - 1} students of his" \
              f"{self.no_of_students} student have sent Birthday gifts."\

student1 = Student("Chan", 13)

print(student1.birthday())


#All instance methods in a class have a parameter called self
#  in their method definition. The address of the object
#  is passed as an argument to this parameter. Unlike other parameters,
#  the value of the argument is provided directly by Python
# 


##When to use instance method 
## When different objects need different values and 
# functionality.We use instance methods to provide
#  unique values and functionality to objects.


