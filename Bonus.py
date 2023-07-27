

def numbers (num:int):
    '''This function print the result as hierarchy only'''
    output =" "
    for i in range(num,0, -1):
        for j in range(i,0, -1):
            print(j,end=" ")
        print(output)
    return(output)        

print(numbers(5))

print(numbers.__doc__)