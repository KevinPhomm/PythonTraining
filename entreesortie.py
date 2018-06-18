
number = input("number : ")


def iterate(n):
    i=0
    n = int(n)
    while i <= n:
        print(i)
        i += 1


def fibonnaci(n):
    list = [0]
    i = 0
    n = int(n)

    while i <=n :
        if list[i] == 0:
            list.append(1)
        else:
            list.append(list[i]+list[i-1])
        i += 1

    print(list)


fibonnaci(number)