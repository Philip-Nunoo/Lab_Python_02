#Philip afful Nunoo
print "Philip Afful Nunoo"
#########################
print "a. x = 2 and y = 5? ",
x = 2
y = 5
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x

##########################
print "b. x = 3 and y = 1? ",
x = 3
y = 1
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
    else:
        print "Nothing"
else:
    print "x is ",x

##########################
print "c. x = 1 and y = 1? ",
x = 1
y = 1
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x

##########################
print "d. x = 4 and y = 3? ",
x = 4
y = 3
if x>2:
    if y>2:
        z=x+y
        print "z is ",z
else:
    print "x is ",x

##########################
##########################
print " "
print "########################################"
print "If x=3 and y = 5 then Y is equal to : ",
x = 3
y = 5

z = x+3
if z==1:
    y=0
elif z==2:
    y=10
elif z==4:
    y+=1
else:
    y=1
print y

#########################

print "If x=3 and y = 5 then Y is equal to : ",
x = 2
y = 5
z = x+3
if z==1:
    y=0
elif z==2:
    y=10
elif z==4:
    y+=1
else:
    y=1
print y

##########################
##########################
print " "
print "########################################"
a = 0
count = 0
i=0
while i < 10:
    count = count + 1
    i+=1
    if i%2 == 0:
        a = a + 1
        print "Output ",a,": ",
        print i
print "Number of times is : ", count


##########################
##########################
print " "
print "########################################"
a = 0
count = 0
i = 0
while i > 10:
    i+=1
    count = count + 1
    if i%2 == 0:
        a = a + 1
        print "Output ",a,": ",
        print i
