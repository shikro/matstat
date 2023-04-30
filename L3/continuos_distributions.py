import random
import math


def rnuni(a, b):
    u = random.uniform(0, 1)
    return (b - a) * u + a


def rnrm1():
    u1 = random.uniform(0, 1)
    u2 = random.uniform(0, 1)
    return math.sqrt(-2 * math.log(u2)) * math.cos(2 * math.pi * u1)


def rnrm2():
    R = 0
    for i in range(0, 12):
        R += random.uniform(0, 1)
    return R - 6


def rnexp(b):
    u = random.uniform(0, 1)
    return -b * math.log(u)


def rnchis(N):
    Y = 0
    for i in range(0, N):
        u = random.gauss(0, 1)
        Y += u ** 2
    return Y


def rnstud(N):
    z = random.gauss(0, 1)
    Y = rnchis(N)
    return z / math.sqrt(Y / N)


def m(data):
    return sum(data) / len(data)


def d(data):
    return sum(map(lambda x: (x - m(data)) ** 2, data)) / len(data)
