class A:
    def __init__(self):
        self.var1=100
        
    def display(self,var1): # This var1 and self.var1 
        #isnot same 
        #self.var1=var1==>> if we had put the value of
        #self.var1 = var1 from display function ans would 
        #be 200
        
        print("class A :",self.var1) 
        # this self.var1 comes from self.var1
        
class B(A):
    def disp2():
        print("class B",self.var1)
    
obj = B()
obj.display(200) # output is 100 not 200

# The result is 100 
'''Because  the child class doesnot   have its own constructor 
but the  parent class have 
so child class will use parent constructor 



'''