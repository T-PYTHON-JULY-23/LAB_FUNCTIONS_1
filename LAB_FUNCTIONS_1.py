
def InvertedNum (number:int):
    ''' The function return the inverted numbers'''
    

    for num in reversed(range(1,number+1)) :
        for num2 in reversed(range(num,number+1)):
             print(num2 , end=" ")

        print("\n")
    
               
         
InvertedNum (5)
















   