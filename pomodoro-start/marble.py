import random


def generate():
    return random.randint(2, m-6)


m = int(input(""))
comb = []

if m < 14 or m > 100:
    raise Exception("Invalid Quantity")
else:
    for i in range((m) ** 5):
        a, b, c, d,e = generate(), generate(), generate(), generate(),generate()
        combination = [a, b, c, d,e]
        if sum(combination) == m and combination not in comb:
            comb.append(combination)
    print(len(comb))
