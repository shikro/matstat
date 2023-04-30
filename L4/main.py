import math
import random


def calc_p(T, L):
    d = 0
    for nn in range(0, N):
        x = []
        for i in range(0, m):
            t = []
            for j in range(0, n[i]):
                t.append(-math.log(random.uniform(0, 1)) / lmbd[i])
            for j in range(0, L[i]):
                l = t.index(min(t))
                t[l] -= math.log(random.uniform(0, 1)) / lmbd[i]
            for j in range(0, n[i]):
                x.append(t[j])
        if not F(x, T):
            d += 1
    return 1 - d / N


def F(t, T):
    return ((t[0] > T) and (t[1] > T) or
            (t[2] > T) and (t[3] > T)) and\
        (t[4] > T) and (t[5] > T) and\
        ((t[6] > T) or (t[7] > T) or (t[8] > T))\
        and ((t[9] > T) or (t[10] > T))


m = 4
eps = 0.005
t_a = 2.576
P = 0.995
N = int(t_a ** 2 * P * (1 - P) / eps ** 2)
n = [4, 2, 3, 2]
lmbd = [10e-5, 10e-6, 80e-6, 30e-6]
T = 8760
min_l_count = float('inf')
res_l = [0] * m
L = [0] * m
f_max = 5
i = 0
while i != f_max:
    L[0] = i
    j = 0
    while j != f_max:
        L[1] = j
        k = 0
        while k != f_max:
            L[2] = k
            l = 0
            while l != f_max:
                L[3] = l
                p = calc_p(T, L)
                if p > P and sum(L) < min_l_count:
                    min_l_count = sum(L)
                    res_l = L.copy()
                if min_l_count == float('inf') and \
                    i == f_max - 1 and \
                    j == f_max - 1 and \
                    k == f_max - 1 and \
                    l == f_max - 1:
                    f_max += 1
                    i = 0
                l += 1
            k += 1
        j += 1
    i += 1

print(f"Min count of spare parts is {min_l_count}")
for i in range(0, 4):
    print(f"L{i} = {res_l[i]}")
