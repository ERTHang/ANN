def N(value, key):
    if key == 1:
        if value == 1:
            return 1.06138074204173
        elif value == 0.5:
            return 1.002538881681694
        elif value == 0.25:
            return 0.982037435779404
        elif value == 0.125:
            return 0.976339831822173
        elif value == 0.0625:
            return 0.974875648960591
        elif value == (0.03125):
            return 0.9745070509058

    pot = 2**(2*(key-1))
    return (pot*N(value/2, key-1) - N(value, key-1))/(pot-1)

for i in range(6,0,-1):
    num = 1
    for j in range(6,i-1,-1):
        print(f"N{i}({num}) = {N(num, i):.14f}\n")
        num/=2
        