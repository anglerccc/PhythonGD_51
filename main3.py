
def getNum(number):
    lst = []
    for i in number:
        if i // 2 == i / 2:
            lst.append(i)
    return lst

print(getNum([1,2,3,4,5,6]))