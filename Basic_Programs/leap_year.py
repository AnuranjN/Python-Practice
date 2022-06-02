# program to check wether leap year

year = int(input("Enter year"))                  #Take input from user

if (year % 400 == 0) and (year % 100 == 0):       #Using conditional statement
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))
