#inheritance ==>> it is the real workd concept extracted 
#It is a feature that enables a class to acquire 
# properties and characteristics of another class.
#

#Inheritance provides code reusaibility 

# for example there look at the below coe 

class User: #this is parent class
    def __init__(self):
        self.name="Atul"
        self.gender= "male"
    
    def login(self):
        print("login")
class student (User):# student class is child class
    pass


s = student()
print(s.name)
print(s.gender)


if __name__ =="main":
    print(main)
