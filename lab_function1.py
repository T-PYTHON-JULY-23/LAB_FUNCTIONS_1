def function1():
    '''function to print number and remove one number every loop'''
    number = [1,2,3,4,5]
    number.reverse()
    for i in number:
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
function1()
print(function1.__doc__)