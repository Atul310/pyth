'''
Inheritance ==>>  

'''
#eg of innheritance 
class User:
    def __init__(self):
        self.name= ""
      
    def login(self):
        print(login)
class Student(User):
    def __init__(self):
        self.roll="3"
    def enroll(self):
        print("enroll int the course")
    
U = User()
s = Student()
print(s.name)
