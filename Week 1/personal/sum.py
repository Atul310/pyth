number = int(input("enter your num: "))
sum =0

for i in range (1,number+1):
    sum=sum+(number%10)
    number=number//10
print(sum)

