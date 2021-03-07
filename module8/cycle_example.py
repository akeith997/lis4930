import itertools

myfile = open('data.txt', 'r')

for n in itertools.cycle(myfile):
    print(n)
