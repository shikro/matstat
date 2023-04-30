import discrete_distributions as dst
import math


def count_tF(a, b, p, N):
    return math.ceil((1 - (1 - p) ** b) * N) - math.ceil((1 - (1 - p) ** a) * N)


def count_eF(a, b, data):
    return len(list(filter(lambda i: a < i <= b, data)))


if __name__ == "__main__":
    N = 50
    p = 0.7
    data = []
    for i in range(0, N):
        data.append(dst.irngeo_1(p))
    low = min(data)
    up = max(data)
    count = 4
    step = 1
    current = 0
    c_t = []
    c_e = []
    while current < up:
        c_t.append(count_tF(current, current + step, p, N))
        c_e.append(count_eF(current, current + step, data))
        current += step
    if up > 4:
        c_t[3] += sum(c_t[3:])
        c_e[3] += sum(c_e[3:])
        c_t = c_t[:4]
        c_e = c_e[:4]
    hi = 0
    for ce, ct in zip(c_e, c_t):
        hi += (ce - ct) ** 2 / ct

    print(f"Theoretical: {c_t}")
    print(f"Empirical: {c_e}")
    print(f"Hi2: {round(hi, 5)}")
