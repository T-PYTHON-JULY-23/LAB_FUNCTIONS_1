
number = int(input("Enter a number"))


def pyramidal_num_print(number:int):
  ''' This function takes a number and then print the numbers from 1 to the giving number pyramidaly and in reverse using two for loops'''
  for i in range(0,number+1): 
         print('\r')
         for j in range(number-i,0,-1):
           print(j,end="")

print(pyramidal_num_print(number))
print(pyramidal_num_print.__doc__)