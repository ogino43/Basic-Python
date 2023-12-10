a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO

for i in [a, b]:
    if i == 1 or i == 3:
        print('%dは素数ではありません。' % i)

    elif i % 2 != 0:
        for k in range(2, (i+1)//2):
            if a % k == 0:
                print('%dは素数ではありません。' % i)
                break
            elif k == ((i+1)//2)-1:
                print('%dは素数です。' % i)
                break

    elif i == 2:
        print('%dは素数です。' % i)

    else:
        print('%dは素数ではありません。' % i)
