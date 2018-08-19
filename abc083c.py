x,y = map(int, input().split(" "))
a = [x]
idx = 0

while True:
    if idx == 0:
        idx += 1
    elif a[idx-1]*2 <= y:
        a.append(a[idx-1]*2)
        idx += 1
    else:
        break

print(len(a))
