

def reverseNumber(number:int) -> str:
    '''This function take a number and return it in reverse order with counting down..'''
    output = ""
    for n in range(number, 0, -1):
        for counter in range(n, 0, -1):
            output += f"{counter} "
        
        output += "\n"
        
    return output
    

print(reverseNumber(5))
print(reverseNumber.__doc__)