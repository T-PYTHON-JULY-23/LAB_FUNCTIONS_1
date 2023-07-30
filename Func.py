num = 5
def patter(num):#this function will take a number and return it as reverse order Step by Step
  for n in range(num, 0,-1):
    for j in range(n, 0,-1):
        print(j, end=" ")
    print('\r')#New line same as (\n) but r is smoother 
    
patter(num)
