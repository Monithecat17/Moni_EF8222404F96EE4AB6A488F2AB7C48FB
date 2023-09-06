#1.2 Write a program that determines whether a year entered by the user is a leap year or not using itelif-else statements.

"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0

"""


def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year : "))

if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))
