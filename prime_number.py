a = float(input("aの値を入力: "))

# TODO


def hantei(n):
    if n.is_integer() is False:
        print("error")
        return False

    elif n <= 0:
        print("error")
        return False

    elif n == 1:
        return False

    elif n == 3:
        return True

    elif n % 2 != 0:
        for k in range(2, (n+1)//2):
            if n % k == 0:
                return False
                break
            elif k == ((n+1)//2)-1:
                return True
                break

    elif n == 2:
        return True

    else:
        return False


print(hantei(a))
