#Philip Afful Nunoo
print "Philip Afful Nunoo"

number = input("Please enter number: ")

number = int(number)

digit = 0
reversednumber = 0
count = number;

while (count != 0):
    reversednumber *= 10
    reversednumber += + (count%10)
    count = count /10

print "The reversed form of {",number,"} is ", reversednumber

count = reversednumber
while (count != 0):
    digit *= 10
    digit += ((count %10 +7) % 10)
    count = count/10
    
print "The {",number,"} is for encryption is ",digit 

count = digit
reversednumber = 0
while (count != 0):
    reversednumber *= 10
    reversednumber += + (count%10)
    count = count /10

print "The encrypted form of {",number,"} is ", reversednumber
