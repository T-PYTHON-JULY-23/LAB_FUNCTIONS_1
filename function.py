def pyramid (x:int)->int:
    '''prints out the result formatted like the pyramid'''

    for row in range(x, 0, -1):
      for col in range(row, 0,-1):
        print(col, end=" ")
    
      print("\n")
        
        
        
pyramid(5)
