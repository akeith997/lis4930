import unittest
import itertools

def repeat_example():
    for n in itertools.repeat('xyz', 100):
        print n

class MyTest(unittest.TestCase):
    def test(self):
        self.repeat_example()
