def Reverse_Order(y):
    """This functions returns an invers pyramid of the numbers"""
    for i in range(y, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


print(Reverse_Order.__doc__)
Reverse_Order(int(input("enter the parameter : ")))
