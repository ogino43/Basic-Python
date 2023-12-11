a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
# TODO

surplus = 0
large = 0
small = 0

if a >= b:
    large, small = a, b
else:
    large, small = b, a

while True:
    surplus = large % small
    if surplus == 0:
        print("最大公約数は%d" % small)
        break
    else:
        large = small
        small = surplus
