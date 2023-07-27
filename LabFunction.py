"""# LAB_FUNCTIONS_1


## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   

### Document the newly created function. describe what it does, then print the documentation. 
"""

def reverse_numbers_printer(number:int) -> None :
    """This function take a number and print all the numbers before it in reverse then do it again but for the number before in new line  
       (upper left triangle ◤ )
       """
    if number < 0 :
        number = number *-1
    if number==0 :
        return
    
    for i in range(number,0,-1):
        print(i,end=" ")
    print()
    reverse_numbers_printer(number-1)
    

reverse_numbers_printer(-5)