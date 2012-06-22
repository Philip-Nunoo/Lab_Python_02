#Philip Afful Nunoo
print "Philip Afful Nunoo"

inputedNumber = raw_input("Please enter number: ")

reversednumber = 0
number =""

#since the inputedNumber is in its raw form
#each digit can be obtained in form ie ((int(n)%10 + 7) % 10)
#the final string value is then converted into integer ie. count = int(number)

for n in inputedNumber:
    number = number + str((((int(n)%10)+7) % 10))
print number

count = int(number)
while (count != 0):
    reversednumber *= 10
    reversednumber += + (count%10)
    count = count /10
print reversednumber

print "The {",inputedNumber,"} for encryption is    : ",number 
print "The encrypted form of {",inputedNumber,"} is : ",reversednumber
