"""
Modify the function you used , so now it returns a string instead of printing directly .
 After calling the function and getting the result, print the result ! 
"""
  
number = 5

def print_format(integer_number:int):
    """This function take integer and return it in reverse pyramid of numbers pattern  sting"""
    word = ""
    for i in range(0, number + 1):
        for j in range(number - i, 0, -1):
           word += f"{j} "
        word+= "\n"

    return word

   
print(print_format(number))
        
print(print_format.__doc__)        
        
        