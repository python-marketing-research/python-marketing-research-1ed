"""
This module contains all function from Chapter 2 of Python for 
Marketing Research and Analytics
"""


def add(a, b=0):
  """Simple addition function
  
  arguments:
  a: value for which addition is defined
  b: value for which addition is defined (optional, defaults to 0)
  
  returns:
  a + b
  """

  return a + b


def check_present(value, values):
  """Check to see if numeric value is present in collection values
  arguments:
  
  arguments:
  value: an object of any type
  values: an iterable object
  
  returns:
  Prints whether or not value was found in values"""

  if value in values:
    print('{} was found in the values'.format(value))
  else:
    print('{} was NOT found in the values'.format(value))


class Adder:
  """A class that adds its parameters
  
  initialization arguments:
  a, b: values for which addition is defined
  
  methods:
  add(): returns the addition of the the parameters x, y"""
  
  def __init__(self, a, b):
    self.x = a
    self.y = b

  def add(self):
    return self.x + self.y
