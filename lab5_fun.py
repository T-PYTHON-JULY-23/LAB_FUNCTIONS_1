def numbers(num:int):


 for i in range(num, 0, -1):
    for n in range(i, 0, -1):
     
     print (n, end="") 
    print()
    
     
numbers(5)
print(numbers.__doc__)
