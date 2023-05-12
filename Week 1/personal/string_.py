# extracting particular character in string 

string = "go away"

# the index is assigned to the string automatically 
# to each of the characters . The index start at the 
#position zero(0). which is called positive indexing 
# goes from left to right 

print(string[2])
# the above print the space  at output

print(string[3])
# space and {a} is printed 


#Another concept is negative index

# to access elements from the last element 
# last character is assigned as -1 
# in above y  is -1
# it goes from  right to left

# The  utility or  function of negative index is that  
#we can take out the last and second last thirdlast ...
# of the string without knowing the length of the string

st = "computer programming, a string is a sequence of characters. For example" 
print(st[-4])


# next concept to take out 
# more than one chararcters from a String 
# The concept is Slice 
# syntax {string[first_index:To which index we want extrac]}

print(st[0:5])

# output is compu

print(st[4:10])
# output is uter p
# here space is also printed

# We can also give third number called step size 

print(st[0:11:2]) 
# output is ==> [cmue r] ==>>
# here it takes 2 jumps and print 
# first 0 position = c  at 2nd taking 2 jumps it prints
# m and u and e then  space and then at last r




''' 
Taking step size with negative 

like a[6:2:-1]

'''


# for negative step first number is big
# like [6:1:-2]



#Negative indexing 

s = 'woe go'
print(s[-6:])