
def Print_number(number):
    '''This function it will print the numbers in revers and in inverted payramid  '''
    for i in reversed(range(1 ,number+1)):
           for j in reversed(range(1 , i+1)):
              print(j , end=" ")
           print("\n")
           
Print_number(5) 
    