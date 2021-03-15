import unittest
import itertools

def count_example():
    for n in itertools.count():
        if 100000 < n < 100010:
            print n
        if n > 1000000:
            break

class MyTest(unittest.TestCase):
    def test(self):
        self.count_example()
