n = int(input())
a = list(map(int, input().split(" ")))
#print(a)
magic = 0
for i in range(len(a)):
    if i == 0:
        continue
    elif a[i] == a[i-1]:
        a[i]=0
        magic += 1

print(magic)
