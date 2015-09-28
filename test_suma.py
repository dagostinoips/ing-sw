#test_suma.py

from suma import *

def test_suma():
  assert suma(10, 3) == 13
  assert suma(5, 5) == 10
  assert suma(2, 3) != 4
