def numbers(x:int):
    ''' pyramid '''
    for i in range(x,0,-1): #x1,x2,x3,x4,x5 
      for j in range (i, 0,-1): #x1,x2,x3,x4
        print(j,end=" ")
      print()
    
numbers(5)   
print(numbers.__doc__)











   



 




 