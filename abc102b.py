n = int(input())
a = list(map(int, input().split(" ")))
#print(a)
ans = max(a) - min(a)
print(ans)
