import discrete_distributions as dst

import matplotlib.pyplot as plt
plt.style.use('ggplot')


def show_gr(data):
    count = 10
    low = min(data)
    up = max(data)
    step = up / count
    current = low
    td = dict()
    while current <= up:
        td.update({current: 0})
        for i in data:
            if current <= i < current + step:
                td.update({current: td[current] + 1})
        current += step

    dd = dict()
    tmp = 0
    for i in td:
        tmp += td[i]
        dd.update({i: tmp})

    for i in td:
        td.update({i: td[i] / len(data) / step})
        dd.update({i: dd[i] / len(data)})

    _, ax = plt.subplots()
    ax.bar(td.keys(), td.values(), width=1*up/count/2)
    plt.title("Dense function")

    p_, ax = plt.subplots()
    ax.bar(dd.keys(), dd.values(), width=1*up/count/2)
    plt.title("Integral function")

    plt.show()


def md(data, M, D):
    m = dst.m(data)
    d = dst.d(data)
    print(f"M = {round(m, 5)}, {round(M - m, 5)}")
    print(f"D = {round(d, 5)}, {round(D - d, 5)}")


def uni():
    M = 50.5
    D = 833.25
    data = dict()
    for i in range(1, 10 ** 4 + 1):
        data.update({i: dst.irnuni(ilow=1, iup=100)})
    md(data.values(), M, D)
    show_gr(data.values())


def bin():
    M = 5.0
    D = 2.5
    data = dict()
    for i in range(1, 10 ** 4 + 1):
        data.update({i: dst.irnbin(n=10, p=0.5)})
    md(data.values(), M, D)
    show_gr(data.values())


def geo(gen):
    M = 2.0
    D = 2.2
    data = dict()
    for i in range(1, 10 ** 4 + 1):
        data.update({i: gen(p=0.5)})
    md(data.values(), M, D)
    show_gr(data.values())


def poi(gen):
    M = 10.0
    D = 10.0
    data = dict()
    for i in range(1, 10 ** 4 + 1):
        data.update({i: gen(mu=10)})
    md(data.values(), M, D)
    show_gr(data.values())


if __name__ == "__main__":
    print("1: irnuni\n2: irnbin\n3:"
          " irngeo_1\n4: irngeo_2\n5:"
          " irngeo_3\n6: irnpoi\n7: irnpsn")
    c = input(">> ")
    match c:
        case "1":
            uni()
        case "2":
            bin()
        case "3":
            geo(dst.irngeo_1)
        case "4":
            geo(dst.irngeo_2)
        case "5":
            geo(dst.irngeo_3)
        case "6":
            poi(dst.irnpoi)
        case "7":
            poi(dst.irnpsn)
        case _:
            print("Unexpected input")
