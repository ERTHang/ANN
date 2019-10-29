def N(value, key):
    if key == 1:
        if value == 1:
            return 21.592933885539452
        elif value == 0.5:
            return 18.55775183335266
        elif value == 0.25:
            return 17.83835666615638
        elif value == 0.125:
            return 17.660441759144206
        elif value == 0.0625:
            return 17.616076336431277
        elif value == (0.03125):
            return 17.60499195111572

    pot = 2**(2*(key-1))
    return (pot*N(value/2, key-1) - N(value, key-1))/(pot-1)

for i in range(6,0,-1):
    num = 1
    for j in range(6,i-1,-1):
        print(f"N{i}({num}) = {N(num, i):.14f}\n")
        num/=2
        