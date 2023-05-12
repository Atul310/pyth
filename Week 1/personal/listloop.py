# Two ways of 
#ItemWise
# IndexWise  


#ItemWise 

l = [1,3,4,5]
for i in l:
    print(i)
'''
Output of above is 
└──╼ $python3 listloop.py
1
3
4
5

and while looping to i 
we find the item only 

loop will run up to last item 

=======================
while looping  among item 
everytime loop runs the value of iterator is that item=====
---------------------------------------------


In above {i} is the iterator and it runs up to the last 
time every time loops run the value of iterator 
{i } is that item 
here  when loop runs  first the  value of first {i}
is {1} {second Time loops run the value of {i} becames}{3}
Third time {It is 4 value of i}
and fourth time { the value of i becames 5 }
and loops teriminate beacsue there are no items to loop 

'''


a = [1,3,4]
for i in a:
    print(a)
'''
Output is ==>>
└──╼ $python3 listloop.py

[1, 3, 4]
[1, 3, 4]
[1, 3, 4]
=======================
Notice Here  while looping throug list 
we found 3 times list 

'''


# IndexWise ==>> It is less in python

j = [1,3,4,5]

for i in range(0,len(j)):
    print(j[i])

'''
Here in above program ==>> 

j is the list with values 
i is the iterator  
i values goes from 0 to length of list 

so do our index value to goes from 
{ 0 to length of list }
when loop runs at first the value of {i} becames
{0} goes to inside loop 
and it print the {j ko value with index 0  is 1}
simarly next { j ko value with index 1 is 3}
simarly next { j ko value with index 2 is 4}
simarly next { j ko value with index 3 is 5}

============================
The output is given of above code 
└──╼ $python3 listloop.py
1
3
4
5


'''