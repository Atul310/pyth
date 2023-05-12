class A:
    def __init__(self):
        self.var1=100
        
    def display(self,var1):
        self.var1=var1
        print("class A :",self.var1)
        
class B(A):
    def disp2():
        print("class B",self.var1)
    
obj = B()
obj.display(200) 
# The result is 100 
'''Because  the child class doesnot   have its own constructor 
but the  parent class have 
so child class will use parent constructor 



'''