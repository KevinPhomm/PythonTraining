def estPremmier(n):

    for i in range(2, n-1):
        if (n % i) == 0:
            return False
    return True


def trouveLesPremiers(limit):
    i = 1
    while i <= limit:
        if estPremmier(i):
            print("%s est premier" % i)
        i += 1


trouveLesPremiers(100)