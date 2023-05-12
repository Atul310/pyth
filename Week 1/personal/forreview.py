#For Loop: A for loop is an iteration method that is best
# used when you know the number of iterations ahead of
# time. It’s always followed by the initialization, 
# expression and increment statements.
#=============================
#==============================
#usecase of For loops
#    • Use a for loop to iterate over an array.
    #Use a for loop when you know the 
   # loop should execute n times.
   #====================================
  
#calculate 1+2+3+..n 
"""
result =0

user_inp = int(input("input number: "))
for i in range(1,user_inp+1):
    result = result+i
    #print(result)
print(result)
"""
#calculate 1/1!+2/2!+3/3!+....n/n!
#applying logic 

# here above n is the value of the input given by user

#let at first we take input from useer 

#n = User_input
result =0
fact = 1
n = int(input("enter the value of n: "))
for i in range(1,n+1):
    fact=fact*i
    result =result+i/fact
print(result)
    




