#A bitwise operator is an operator used to perform 
# bitwise operations on bit patterns 
# or binary numerals that involve 
# the manipulation of individual bits. 

#Bitwise is a level of operation that involves working 
# with individual bits which are the smallest units of 
# data in a computing system. Each bit has single binary 
# value of 0 or 1. Most programming languages 
# manipulate groups of 8, 16 or 32 bits. 
# These bit multiples are known as bytes.

#Computers store all kinds of information as a stream of 
# binary digits called bits. Whether you’re working with text, 
# images, or videos, they all boil down 
# to ones and zeros. Python’s bitwise operators let you manipulate 
# those individual bits of data at the most granular level.

'''You can use bitwise operators to implement algorithms 
such as compression, encryption, and error detection as 
well as to control physical devices in your Raspberry Pi 
project or elsewhere. Often, Python isolates you from the 
underlying bits with high-level abstractions. You’re more 
likely to find the overloaded flavors of bitwise operators 
in practice. But when you work with them in their original form, 
you’ll be surprised by their quirks! '''

 # bitwise operator types 
 #1) And (&)
 #2) or (|)
 #3) not (~)
 #4) xor (^)
 #5) left shift () and right shift()
 
print(1&2)
# The output is 0
# by converting into binary we know 
#   1 =   01
#   2 =   10
#--------------
#         0 0 
# so output is 0
#The and opertion gives 
#  
print(2 | 3)

# output is 2 
# 2 = 10
# 3 = 11
#-----------
#     11 ==>> 3
# 11 in decimal is 3

print (2 ^ 4)
# out put is 4
# doing Xor in  2 ra 4 ma
# 2 = 010
# 4 = 100
#----------
#     110 ==>> 6
# 110 in decimal is 6 
#  in xor opeation if two bits are same then it will be
#(0) zero
# if 2 bits are different then the output will be 1



# Left shift and right shift (remaining)


#################################

##Membership operator ==>>
''' 
Membership operator ==>> use to check whether certain 
sequence such as string list tupels are present in membership or 
not 

Two types 
1) in 
2 ) not in 

in==>>
in	By using the in operator, one can determine if 
a value is present in a sequence or not. If the
specified variable/literal is found, it will return true, 
otherwise, it will return false.



not in ==>>not in	By using the, not in operator,
one can determine if a value is not present in a sequence 
or not. If the specified variable/literal is found, 
it will return false, otherwise it will return true.



'''
item = 29 ## Output is true
item = 30 ## output is False # 30 is not presernt 
list_1 = list(range(1, 30))
print(item in list_1)






st = "Atul "
st+= " Dhital"
print(st)