import random
import math


def irnuni(ilow, iup):
    u = random.uniform(0, 1)
    return math.floor((iup - ilow + 1) * u + ilow)


def irnbin(n, p):
    if n >= 100:
        return math.floor(random.gauss(n * p, math.sqrt(n * p * (1 - p))) + 0.5)

    M = random.uniform(0, 1)
    r = 0
    P = (1 - p) ** n
    M -= P
    while M >= 0:
        P *= (n - r) / (r + 1) * (p / (1 - p))
        M -= P
        r += 1
    return r


def irngeo_1(p):
    M = random.uniform(0, 1)
    P = p
    r = 0
    while M >= 0:
        M -= P
        P *= 1 - p
        r += 1
    return r


def irngeo_2(p):
    k = 1
    M = random.uniform(0, 1)
    while M > p:
        M = random.uniform(0 , 1)
        k += 1
    return k


def irngeo_3(p):
    u = random.uniform(0, 1)
    q = 1 - p
    return math.floor(math.log(u) / math.log(q)) + 1


def irnpoi(mu):
    if mu >= 88:
        return math.floor(random.gauss(mu, mu) + 0.5)

    P = math.exp(-mu)
    M = random.uniform(0, 1) - P
    r = 0
    while M >= 0:
        r += 1
        P *= mu / r
        M -= P
    return r


def irnpsn(mu):
    if mu >= 88:
        return math.floor(random.gauss(mu, mu) + 0.5)

    e = math.exp(-mu)
    M = random.uniform(0, 1)
    k = 0
    while M >= e:
        k += 1
        M *= random.uniform(0, 1)
    return k


def m(data):
    return sum(data) / len(data)


def d(data):
    return sum(map(lambda x: (x - m(data)) ** 2, data)) / len(data)
