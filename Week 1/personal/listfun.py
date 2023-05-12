#adding item in list 
# Three ways 
#1) append() function 
# extend() function 
# insert function 

# append will add one item at  a time at last pos in list 
# extend() will add multiple item in the list 
l = ["a", 2,4,5] 
print(l)  # output==> ['a', 2, 4, 5]
l.append("sa")

print(l) # output ==>['a', 2, 4, 5, 'sa']


#extend

l2 = [1,2,3,"shady", "gp"]
l2.extend("shady")
print(l2) # output is 
#[1, 2, 3, 'shady', 'gp', 's', 'h', 'a', 'd', 'y']

#insert() function  ==> It is used to add 
# item in desired index 
# but one item at a time 

l3 = [23,4,3,"gh",[]] # output is 
# 
l3.insert(1, "object")
print(l3) ##output is ==>>
#[23, 'object', 4, 3, 'gh', []]

## editng item in list 

# list are mutable 
# means we can edit list at dynamic time 
# we can add elements value ,
# modify the elements value 
# individual value can be replaced 

#edit value 
a = [1,3,4,500]
a[3] =300
print(a)
# output is ==>> [1, 3, 4, 300]
# at index three 500 changes to 300 
# which is mutabilatiy 
# We can modify multiple items by using slcing function
# also by the negative indexing 



#deleting in list ]==>> using del keyword






#=====================

##operator in list 
# arithmetic 
#addition(+)
c = [1,3,4,5]
d = ["shady",75]
print(c+d)
# it will concatenate 
# another word for concatenating here is merging 
# output ==>> [1, 3, 4, 5, 'shady', 75]
#=======================
# Multiplaction 
print(c*3)
# [1, 3, 4, 5, 1, 3, 4, 5, 1, 3, 4, 5]


## loop in list 
u = [[1,"Atul",23,"cyber"] ,[ 2,"Atul",21,"se"] ,[ 3,"Atul",21,"hr"]]
for i in u:
    print(u[0],[i])