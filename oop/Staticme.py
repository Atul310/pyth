# static method ==>>  methods that perform operation on 
#external data  


#external data  means not associated to class and 
#objects (data outside)

# There is no need to give  object and class refrence to 
#access and modifiy 





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#it can also perform operation on static varable(class-level)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##static method are strictly for external data 


#created by using  
# @staticmethod decorator
class Bank:
    bank_name="b"
    rate_of_interest = 12
    @staticmethod
    def find_interest(prin,t):
       si = (prin*t*Bank.rate_of_interest)/100
       print(si)
        
        
    
Bank.find_interest(1000,2)

     


        

        
    
    
    


        
        




