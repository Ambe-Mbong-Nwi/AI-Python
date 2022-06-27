# right angled triangles(RAT)
def RAT(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001
    # example
print(RAT(3, 4, 5))