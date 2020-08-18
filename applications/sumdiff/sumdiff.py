"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def add(a, b):
    return f(a) + f(b)

def subtract(c, d):
    return f(c) - f(d)

tups = {}

min = float("inf")

for a in range(len(q)):
    for b in range(a, len(q)):
        key = (q[a], q[b])
        result = add(q[a], q[b])

        if result < min:
            min = result

        if result not in tups:
            tups[result] = []

        if key != (q[b], q[a]):
            tups[result].append((q[b], q[a]))

        tups[result].append(key)

for c in range(len(q) - 1, -1, -1):
    for d in range(c, -1, -1):
        key = (q[c], q[d])
        result = subtract(q[c], q[d])

        if result in tups:
            for element in tups[result]:
                print(element, key, result)
    if result < min:
        break
