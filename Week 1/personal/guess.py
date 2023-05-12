#guessing game 

import random
jackpot_number =random.randint(0, 100)

# jackpot_number is the number random number selected 
#by computer 
#
# user_input is the number input through keybord

user_input = int (input("guess yor number: "))
count = 1
while user_input != jackpot_number:
 if user_input < jackpot_number:
    print("Sorry your  guess is less than the number. guess higher: ")
    
 else :
    print("your number is higher ")
 user_input= int(input("guess again: "))
 count+=1

else :
    print("correct guess")
    print("you guess correct in ", count , "attempts")


    

 

    


