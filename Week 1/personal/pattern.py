# we print by asking to the usere 
# taking user input 
# We print via rows


#one loop handle how many rows to print 
# and another loops handle the * to be printed 
#


rows = int(input("input no of rows to print "))
#if user says five rows there should be five * in the 
# last row 

for i in range(1,rows+1):
    #print("*")
    for j in range(1,i+1):
        print("*",end="")
    print()
 

    
    
''' 
i+1 because ==>> our * print up to which the value of
  i is 
 
 # here if the user input the rows 5 
 # our i becames (1,6) because rows =5 
 rows+1 = 6
 
 
 
 
 

'''  