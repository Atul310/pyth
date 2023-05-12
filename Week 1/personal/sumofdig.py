# find the sum of 3 digit number input by user

'''
print(345/10) ## it gives 34.5
it is normal division
It works on integer and float both 

##################################
print(345//10) ## it gives 34 only 
becuse it is integer division 

'''

user_inp = int(input("enter number: "))

a = user_inp%10
# takes out last number 
# this is 1st step

user_inp= user_inp//10
# breaks into 2 number 
# this is second step

b = user_inp%10
# itakes number from second step 
#takes out the 2nd number 
# third step 

user_inp = user_inp//10
# takes from third step 
# break into 1 number 

c = user_inp%10
# takes out from third step 
# takes out one number 

sum = a+b+c
print("the sum is",sum)


