
'''Bonus (Not Required):  using the last lab (LAB_FUNCTIONS_1) create   another file:
Modify the function you used , so now it returns a string instead of printing directly . 
After calling the function and getting the result, print the result !'''
def numbers (num:str ):
    '''This function print the result as hierarchy only'''
    output =""
    for i in range(num,0, -1):
        for j in range(i,0, -1):
            output += str(j)+' '
        output+='\n'            
        
    return(output)        

print(numbers(5))

print(numbers.__doc__)
