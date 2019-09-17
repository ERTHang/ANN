def func(x):
    return 2 + 7.94/(x**2+6)


def devfunc(x):
    return -7.94*2*x/(x**2+6)**2


print("|g'(x)| < 1")
print(f"{abs(devfunc(3)):.4f} < |g'(x)| < {abs(devfunc(2)):.4f}")
print()
p = 2.92
for i in range(8):
    print(f"p{i+1} = {p:.7f}")
    p = func(p)
print()
print("f(x) = x ^ 3 - 2x ^ 2 + 6x - 19.94",
      "g(x) = 2 + 7.94 / (x ^ 2 + 6)",
      "g(x) = x",
      "2 + 7.94 / (x ^ 2 + 6) = x",
      "7.94 / (x ^ 2 + 6) = x - 2",
      "7.94 = (x ^ 2 + 6) * (x - 2)",
      "7.94 = x ^ 3 - 2x ^ 2 + 6x - 12",
      "0 = x ^ 3 - 2x ^ 2 + 6x - 19.94",
      "f(x) = 0", sep="\n")
