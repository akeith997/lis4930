import unittest
import itertools

def cycle_example():
    myfile = open('data.txt', 'r')
    
    for n in itertools.cycle(myfile):
        print(n)

class MyTest(unittest.TestCase):
    def test(self):
        self.cycle_example()
