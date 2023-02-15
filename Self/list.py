##list 
marks = [0,1,2,35,5]

print(marks[0])    ##accessing the element of list
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
#marks.append()
## if we have negative indexing convert it to positive 
##by using len() function 


# print the -3 from list

##imp
print(len(marks)-3) ## converting to ppositive 


## to know if the element is present in the pist ornot


## in keyword use

if 35 in marks : 
    print (True)
else:
    print(False)



'''
list_of_people = ["atul",30, "value",20, "cool"]
for index,i in enumerate(list_of_people):
    print(index,i)

'''




## using slicing [:]
print(marks[:])  ### all marks are printed
#[:] first value is 0 last is up to the list index
# [0:len(marks)]

print(marks[0:-1])
# the  [-1] is being sliced 
# and poped out 
# output is [0,1,2,35]

# when we see negative index convert into positive 


#[::]
# list also works in 3 aguments 


l =["shady ", 1, 4,"Messi",7,10]
# print the list in such way that 
## [10,messi]


#print in reverse order such that output is
# [10,Messi]
print(l[-1:-4:-2])
print(l[0]) ## takes the indvidual element of the list 


#to use for loop with range we need  int type data 
## iterating over list using for loop range 
a = [10,2,3,56,7]
for i in range(len(a)):
    print(a[i])



#  i is the iterator which generates the number from 
# index start from 0 to the  length of string 


# a[i] means a[0]==>>10
# a[i] means a[1]==>> 2
#....
#a[len(a)[i]]


##another way of iterating in list 

## dirctly passing the list 
for index,i in enumerate(a):
    print(index,i)
