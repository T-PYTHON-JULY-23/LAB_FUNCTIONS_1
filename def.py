def numbers_hierarchy(x:int):
    '''The function Will be print the numbers in hierarchy'''
    for f in range (x,0, -1):
        for i in range(f,0, -1):
            print(i,end=" ")
        print()

numbers_hierarchy(5)

print(numbers_hierarchy.__doc__)