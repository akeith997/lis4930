import itertools

for n in itertools.count():
    if 100000 < n < 100010:
        print n
    if n > 1000000:
        break
