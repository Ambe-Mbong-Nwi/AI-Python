# right angled triangles(RAT) and extension for sides to be given in any order.
def RAT(a, b, c):
    if a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    elif b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
    # example
print(RAT(3, 4, 5))
print(RAT(5, 3, 2))