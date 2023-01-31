#easy edabit questiom 
'''
Write a function that stutters a word as if someone is struggling to read it. 
The first two letters are repeated twice with an ellipsis 
... and space after each, and then the word is pronounced with a question mark ?.
'''

def strutter (word):

    return (f"{word[:2]}... {word[:2]}...{word}?")

print(strutter("what"))

##problem 2
'''
Create a function that takes two arguments: the original price
 and the discount percentage as integers and returns the final
  price after the discount.

'''
def price(p1,d):
    disc= (d/100)*p1
    priceafterdis= p1-disc
    return priceafterdis


print(price(10000,10))
#Your answer should be rounded to two decimal places.


#problem 3
'''
Given the radius of a circle and the area of a square,
 return True if the circumference 
of the circle is greater than the square's 
perimeter and False if the square's perimeter is greater
 than the circumference of the circle.

'''
from math import sqrt
def myFun(rad,area):
    c= 2*3.14*rad
    perimeter= 2 *sqrt(area)
    if c>perimeter:
        return True
    else :
        False 

print(myFun(1,3))


