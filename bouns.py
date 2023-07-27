def pyramid (x):
    
    '''prints out the result formatted like the pyramid'''
    string=""

    for row in range(x, 0, -1):
      for col in range(row, 0,-1):
        string=string+str(col)+" "
     
      string=string+"\n"
    
    return string


print(pyramid(5))
        