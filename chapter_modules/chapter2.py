'''
This module contains all function from Chapter 2 of Python for 
Marketing Research and Analytics
'''


def add(a, b=0):
  '''Simple addition function'''
  return a + b


def check_present(value, values):
  '''Check to see if numeric value is present in collection values'''
  if value in values:
    print('{} was found in the values'.format(value))
  else:
    print('{} was NOT found in the values'.format(value))


class Adder:
  '''A class that adds its parameters'''
  def __init__(self, a, b):
    self.x = a
    self.y = b

  def add(self):
    return self.x + self.y
