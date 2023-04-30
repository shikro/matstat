import math
import numpy.random as rnd


N = 50
alpha = 0.05
X = rnd.default_rng().triangular(0, 1, 2, N)
Y = rnd.default_rng().normal(1, 1, N)

w = 0
for x, y in zip(X, Y):
    if x == y:
        N -= 1
    elif x > y:
        w += 1

b = 2 ** (-N) * sum([math.comb(N, i) for i in range(0, w + 1)])

print(f"N = {N}")
print(f"w = {w}")
print(f"alpha = {alpha}")
print("H0  : P{X > Y} = 1/2")

if not (alpha / 2 <= b <= 1 - alpha / 2):
    print("H1  : P{X > Y} != 1/2 is true")
    print("Then H0 is false")
    exit()

print("H1  : P{X > Y} != 1/2 is false")
print("Then H0 is true")
