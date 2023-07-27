def Reverse_Order(y):
    for i in range(y, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


Reverse_Order(int(input("enter the parameter : ")))
