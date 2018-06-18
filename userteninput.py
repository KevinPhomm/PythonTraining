def max(list):
    max = 0
    for i in list:
        if i > max :
            max = i
    return max

def userInput():
    value = input("Entrez un nombre ")
    if value == "":
        value = 0
    return int(value)

def initUserList(limit):
    userList=[]
    print("Vous allez entrer %s nombres" % limit)
    for i in range(0,limit):
        userList.append(userInput())
    return userList


def main():
    myuserList = initUserList(10)
    print("Le chiffre max est %s" % max(myuserList))


main()