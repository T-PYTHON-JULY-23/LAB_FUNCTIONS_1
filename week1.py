def ArrayNumbers(number:int):
    ''' a function that takes 1 parameter of type int , 
    then it prints out the result of some formatted shape '''

    
    for iteration in range(number,0,-1):
            for iteration2 in range(iteration,0,-1):
    
              print (iteration2,end=" ") # to delete the new line and make all the output itteration in one line
            print("")
    




inputNumber=int(input("Enter a number to show to array:"))
ArrayNumbers(inputNumber)