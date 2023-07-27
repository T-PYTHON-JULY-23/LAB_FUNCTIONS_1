"""# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   

### Document the newly created function. describe what it does, then print the documentation. 
"""

def reverse_numbers_printer(numbers:int) -> None :
    """This function take a number and print all the numbers before it in reverse then do it again but for the number before in new line  
       (upper left triangle ◤ )
       """
    full_stirng=''
    number_for_lines=numbers


    for line in range(0,numbers):
        for number in range(numbers,0 , -1 ):
            full_stirng= full_stirng + str(number) +" "
        full_stirng=full_stirng +"\n"
        numbers-=1

            
    full_stirng=full_stirng[:-1]
    return full_stirng

    


    
up_left_triangle=reverse_numbers_printer(5)
print(up_left_triangle)