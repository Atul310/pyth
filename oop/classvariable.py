## class level variable 
# static variable 
# made for entire class  and for all object 


#3 we can access the class (static variable ) by using 
#object refrence too .
##butt.... we cannot modify the class varaiable(staticvaruiable)
#by using object refrence 

##acessing  and modifying class variable by 
#class method
# to write class methood we use @classmethod

# @classmethod  
# def method_name(cls) ==>  cls is class refrecne 
#we also can write classname but for general convenction

class Employee :
    compant_name = "abd"
    @classmethod
    def change_company_name(Employee):
        Employee.compant_name="abc" 
        print("Modified ",Employee.compant_name)       

Employee.change_company_name()
    







