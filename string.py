##string oloop

name = "atul"
for index,i in enumerate(name):
    print(index,i)



## to find length of string  using function 

st = "atul is good"
#print(len(st))


##to find length of string without using function 
a = 0
for i in st:
    a =a+1

print(a)
  # in above program 



  ##iterating string 
w ="welcome"
t = len(w)
print(t) #7
for a in range(t):
    print(w[a])
# a runs up to 7 because we have range =7
## w[a] means +=>> 
## here a is the iterator 
# a is loop number 
## we use  a index number 
# at first when a is passed in w 
#like w[a] ==.. it is read as w[0] = w prints 
# then it goes to w[1] ...w[6]e and after it goes to 
# w[7] it does not find and terminates
# and print
 