def F(x):
    return [(x[0]**2 - 3 * x[1]**2 + 5), (x[0]**2 + 2 * x[1]**2 - 5)]


def JF(x):
    yaux1 = [2*x[0], -6*x[1]]
    yaux2 = [2*x[0], 4*x[1]]
    return [yaux1, yaux2]


def inv(x):
    yaux1 = [4*x[1], 6*x[1]]
    yaux2 = [-2*x[0], 2*x[0]]
    return [yaux1, yaux2]


def det(y):
    return y[0][0] * y[1][1] - y[0][1] * y[1][0]


x = [1.69, 1.17]

for i in range(3):
    print(f"X{i + 1}")
    print(*[round(i, 8) for i in x])

    r = [0, 0]

    for y in range(2):
        r[y] = inv(x)[y][0] * F(x)[0]
        r[y] += inv(x)[y][1] * F(x)[1]
        r[y] *= (1 / det(JF(x)))

    x[0] -= r[0]
    x[1] -= r[1]

print(f"X4")
print(*[round(i, 8) for i in x])
