#Philip Afful Nunoo
print "Philip Afful Nunoo"

number = input("Please enter number: ")

number = int(number)

reversednumber = 0
count = number;

while (count != 0):
    reversednumber *= 10
    reversednumber += + (count%10)
    count = count /10

print "The reversed form of {",number,"} is ",reversednumber
