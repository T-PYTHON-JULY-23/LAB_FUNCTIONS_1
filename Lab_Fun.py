
   
number = 5

def print_format(integer_number:int):
    """This function take integer and print it in reverse pyramid of numbers pattern"""
    for i in range(0, number + 1):
        for j in range(number - i, 0, -1):
            print(j, end=' ')
        print()


   
print_format(number)
        
print(print_format.__doc__)        
        
        
 