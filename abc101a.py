s = list(input())
#print(s)
i = 0
for si in s:
    if si == "+":
        i += 1
    else:
        i -= 1

print(i)
