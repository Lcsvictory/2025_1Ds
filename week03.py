import random

this_week_winner = [17,18,23,25,38,39]

def random_sixnum():
    result = set()
    while len(result) != 6:
        result.add(random.choice(range(1,46)))
    return list(result)

def iters(l1, l2):
    l3 = [value for value in l1 if value in l2]
    return l3

def intersect(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    return list(l1 & l2)

def unio(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    return list(l1 | l2)

def diff(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    return list(l1 - l2)

print(intersect(this_week_winner, random_sixnum()))
print(unio(this_week_winner, random_sixnum()))
print(diff(this_week_winner, random_sixnum()))

