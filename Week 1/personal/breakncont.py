# Break is used to contorl the flow of loops
# Real life scenario 

'''
Suppose we have to search for a person in a database
with the id person id (unique key i.e primary key) 

we use break statement here to search 

if the person id = found then break the statement 
which avoid searching for after that id 

imagine we have 1000 no of people enntry in database
and the person we search for it at n0 58 


# then loop will runs until the no is found 
if no is found then 
break statemnt will exit out of loop



'''


# making a program to search for number given by useer
"""
user_inp = int(input("enter your numer to search: "))
for i in range(1,1000):
    if i == user_inp:
        break
    #print(i)
print("the number you serached is",i)
"""



##continue +=>> it is used to skip the current given 
#situatuon 

for i in range (1,6):
    if i ==4:
        continue
    print(i)
    