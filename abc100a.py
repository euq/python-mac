#食べたい数のケーキを取ることができるならば Yay!, そうでなければ :( と出力しなさい.
a, b = map(int, input().split(" "))
if (a < 9) & (b < 9):
    print("Yay!")
else:
    print(":(")
