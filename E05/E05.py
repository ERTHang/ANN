a = [-3.8, -0.2, -2.3, -0.8, 2.9]

print("iteraçoes:")

for i in range(1, 10):
    print(f"X{i}")
    print(*[round(i, 8) for i in a], sep=', ')
    a[0] = ((-2.5*a[1]+0.7*a[2]-2.5*a[3]-1.7*a[4]-4.8)/9.7)
    a[1] = ((-2.6*a[0]-1.9*a[2]+2.0*a[3]+2.9*a[4]-3.8)/9.7)
    a[2] = ((-0.7*a[0]-0.6*a[1]-1.6*a[3]+2.3*a[4]-2.9)/13.9)
    a[3] = ((-1.1*a[0]-0.5*a[1]+1.7*a[2]-0.9*a[4]+3.6)/5.5)
    a[4] = ((2.6*a[0]+1.7*a[1]-3.0*a[2]+2.6*a[3]-4.6)/11.1)

print("X10 e resultado final:")

print(*[round(i, 8) for i in a], sep=', ')
