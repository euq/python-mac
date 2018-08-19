t =  int(input())
for i in range(t):
    a[i] = list(map(int, input().split(" ")))

for ai in a:
    aia = ai[0]
    aib = ai[1]
    aic = ai[2]
    aid = ai[3]
    stock = aia
    while stock < 10**18:
        if stock < aib:
            print(No)
            brflag = "True"
            break
        elif:
            stock -= aib
            if stock <= aic:
                stock += aid
    if brflag "True":
        break
    print("Yes")
