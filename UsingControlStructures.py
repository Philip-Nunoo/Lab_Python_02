#Philip Afful Nunoo

print "Philip Afful Nunoo"
print "Question 5"

theInput = raw_input("Enter an integer: ")
#Your code here

number = int(theInput)

if (number % 2 == 0):
    print "The Number(",theInput,") is even"
else:
    print "The Number(",theInput,") is odd"

print " "
print "--------------------------------------"
print "Question 6"
print ""
print "Primary School Age               : 4"
print "Legal vote age                   : 18"
print "Age for aspiring for presidency  : 40"
print "Age for retirement               : 60"
primarySchoolAge = 4
legalVoteAge = 18
presidentRequiredAge = 40
offRetirementAge = 60
personsAge = input("Enter an age : ")

if (personsAge >= primarySchoolAge):
    if (personsAge >= legalVoteAge):
        print "Remember to vote."
        if (personsAge >= offRetirementAge):
            print "Too old. You need to retire"
        elif( personsAge == presidentRequiredAge):
            print "Vote for me"
        else:
            print "You cann't be president"
    else :
        print "You cann't vote now."
else :
    print "Too young !!"


print " "
print "--------------------------------------"
print "Question 7"

multiples = ""

product =""
i = 40
j = 1
while (i>=0):
    if ( i % 3 == 0):
        print i, " ",
    i -=1

print " "
print "--------------------------------------"
print "Question 8"

print ""
print "The numbers that are not divisible by 2,3 and 5 between  6 and 30 are: "
print "     {",
for i in range(6,30,1):
    if( i % 2 != 0):
        if (i % 3 != 0):
            if(i % 5 != 0):
                print i, " ", 
print "}"


print " "
print "--------------------------------------"
print "Question 9"

print "The smallest positive integer n such that 79*n"
print "has a remainder of 1 when divided by 97 is: "
n=1
while n >0:
  n = n+1
  ans = (n*79)%97
  if ans == 1:
    print n, 'breaking out of loop'
    break
