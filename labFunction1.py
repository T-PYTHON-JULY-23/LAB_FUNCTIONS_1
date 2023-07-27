
number = int(input("enter a number: "))


def pattern (number):
    '''This function takes 1 parameter of type int and print it as a pattern '''
    for i in range(0,number):
        for j in range(number-i,0,-1):
            print(j, end=" ")
        print()
    
pattern(number)

print(pattern.__doc__)