import random, math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

lookup_table = {}

def create_lookup_table(x, y):
    for i in range(2, 15):
        for j in range(3, 7):
            lookup_table[(i, j)] = 0

    for (x, y) in lookup_table.keys():
        lookup_table[(x, y)] = slowfun_too_slow(x, y)
        print(lookup_table[(x, y)])


def slowfun(x, y):
    if len(lookup_table) < 1:
        create_lookup_table(x, y)
    else:
        return lookup_table[(x, y)]
        
    print(lookup_table)

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
