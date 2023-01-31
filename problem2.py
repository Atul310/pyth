###edabit easy 
#Luke Skywalker has family and friends. Help him remind them who is who. 
# Given a string with a name, return the relation of that person to Luke.

"""
Person 	        Relation
Darth  Vader 	father
Leia	        sister
Han	            brother in law
R2D2	        droid

"""

class Relation:
    def __init__(self,name,relation) -> None:
        self.n=name
        self.r =relation

p1 = Relation("Darth vader","father")

print("Luke I am Your ",p1.r)

## Do it another way 







## problem 6

''' 
Create a function that takes an array of values resistance
 that are connected in series, 
and calculates the total resistance of the circuit in ohms. 
The ohm is the standard unit of electrical resistance in 
the International System of Units ( SI ).

   '''
def Ressistance(list):
    list=[1,3,4,5]
    










#problem 7
'''
Solving Exponential Equations With Logarithms
a =b **x
log(sbustring b) a = x

Create a function that takes a number a and finds the missing exponent x 
so that a when raised to the power of x is equal to b.


'''
def   exponent(a,b):
