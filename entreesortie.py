
#number = input("number : ")


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

    while i < n-1 :
        if list[i] == 0:
            list.append(1)
        else:
            list.append(list[i]+list[i-1])
        i += 1

    return list


# print(fibonnaci(number))

def isValueInList(value, list):
    value = int(value) #str to int
    return value in list


# value = ie, gunput("Devinez une valeur dans le tableau : ")
# # guesslist = [1,2,3]
# # if isValueInList(valuesslist):
#     print("la valeur est dans le tableau" )
# else:
#     print("Ah bah non dommage !")


def isIndexOf(v, list):
    index=0
    listindex = []

    for i in list :
        if i == v:
            listindex.append(index)
        index += 1
    return listindex


# print(isIndexOf(int(value), guesslist))

def isPalindrome(str) :
    str_reverse = ""
    for i in range(len(str)-1, -1, -1):
        str_reverse += str[i]
    return str_reverse == str


if isPalindrome("kayak"):
    print("c'est un palindrome")
else:
    print("ce n'est pas un palindrome")