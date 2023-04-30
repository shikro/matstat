import continuos_distributions as dst

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
    print(f"E(t) = {round(m, 5)}, {round(M - m, 5)}")
    print(f"V(t) = {round(d, 5)}, {round(D - d, 5)}")


def show(M, D, gen):
    data = []
    for i in range(0, 10 ** 4):
        data.append(gen())
    md(data, M, D)
    show_gr(data)


if __name__ == "__main__":
    print("1: rnuni\n2: rnrm1\n3:"
          " rnrm2\n4: rnexp\n5:"
          " rnchis\n6: rnstud")
    c = input(">> ")
    match c:
        case "1":
            show(50.5, 833.25, lambda: dst.rnuni(1, 100))
        case "2":
            show(0, 1, dst.rnrm1)
        case "3":
            show(0, 1, dst.rnrm2)
        case "4":
            show(1, 1, lambda: dst.rnexp(1))
        case "5":
            show(10, 20, lambda: dst.rnchis(10))
        case "6":
            show(0, 1.25, lambda: dst.rnstud(10))
        case _:
            print("Unexpected input")
