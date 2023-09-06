# Leap Year

"""
Year % 4 == 0 &
Year % 100 ! 0 /
Year % 400 == 0

"""
def isleapyear(year):
   if (year % 4 == 0 and Year % 100!= 0) or year % 400 == 0:
     return True 
   else:
    return False

year = 2022

if isleapyear(year):
   print('{} is a leapyear.'.format(year))
else:
  print('{} is not a leapyear.'.format(year))
  
