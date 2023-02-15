with open("python.txt","r") as file:
 wri=file.readlines( )
 print(wri)

 # readlines method 
word = 'hello'
letter0 = list(word)
print(letter0)


## split() method  ==>> it divide the string into list 

line = "metazone: the Happy zone"
val = line.split(" ") # delimeter is the value or something passed 
#inside .split(" delimeters") <<==
print(val)