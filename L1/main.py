import math
import random

import matplotlib.pyplot as plt
plt.style.use('ggplot')


if __name__ == "__main__":
    u = [0]
    print("Generating data...")
    while len(u) != 10 ** 4 + 1:
        u.append(random.uniform(0, 1))

    print("Calculating M...")
    M = dict()
    for i in range(1, 5):
        M.update({i: sum(u[1:10 ** i + 1]) / 10 ** i})
        print(f"M{i} = {round(M[i], 5)}, {round(0.5 - M[i], 5)}")

    print("Calculating D...")
    D = dict()
    for i in range(1, 5):
        D.update({i: sum(map(lambda x: (x - M[i]) ** 2, u[1:10 ** i + 1])) / 10 ** i})
        print(f"D{i} = {round(D[i], 5)}, {round(0.08333 - D[i], 5)}")

    print("Calculating S...")
    S = dict()
    for i in range(1, 5):
        S.update({i: math.sqrt(D[i])})
        print(f"S{i} = {S[i]}")

    print("Calculating K[f]...")
    K = dict()
    for i in range(1, 5):
        K.update({i: dict()})
        n = 10 ** i
        for f in range(1, n + 1):
            a = sum([(u[j] - M[i]) * (u[j + f] - M[i]) for j in range(1, n - f + 1)])
            b = sum([(u[j] - M[i]) ** 2 for j in range(1, n + 1)])
            K[i].update({f: a / b})

        _, ax = plt.subplots()
        ax.bar(K[i].keys(), K[i].values())

    sorted_u = sorted(u[1:])
    count = 100
    step = 1 / count
    current = 0
    td = dict()
    while current <= 1:
        td.update({current: 0})
        for i in sorted_u:
            if current <= i < current + step:
                td.update({current: td[current] + 1})
        current += step

    dd = dict()
    tmp = 0
    for i in td:
        dd.update({i: tmp})
        tmp += td[i]

    for i in td:
        td.update({i: td[i] / 10000 / step})
        dd.update({i: dd[i] / 10000})

    _, ax = plt.subplots()
    ax.bar(td.keys(), td.values(), width=0.005)

    _, ax = plt.subplots()
    ax.bar(dd.keys(), dd.values(), width=0.005)

    plt.show()
