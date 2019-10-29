def N(value, key):
    if key == 1:
        if value == 1:
            return 23.1247897332
        elif value == 0.5:
            return 7.7951871619
        elif value == 0.25:
            return 3.9365614951
        elif value == 0.125:
            return 2.6382263768
        elif value == 0.0625:
            return 2.104908111
        elif value == (0.03125):
            return 1.8628127355
        else:
            return 1.7474155883

    pot = 2**(key-1)
    return (pot*N(value/2, key-1) - N(value, key-1))/(pot-1)

for i in range(7,0,-1):
    num = 1
    for j in range(7,i-1,-1):
        print(f"N{i}({num}) = {N(num, i):.10f}\n")
        num/=2
        