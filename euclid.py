a1 = int(input("a の値を入力: "))
b1 = int(input("b の値を入力: "))
# TODO


def euclid(a2, b2):
    surplus = 0
    large = 0
    small = 0

    if a2 >= b2:
        large, small = a2, b2
    else:
        large, small = b2, a2

    while True:
        surplus = large % small
        if surplus == 0:
            return small
            break
        else:
            large = small
            small = surplus


def tagainiso(a3, b3):
    if euclid(a3, b3) == 1:
        return True
    else:
        return bool


print(tagainiso(a1, b1))
