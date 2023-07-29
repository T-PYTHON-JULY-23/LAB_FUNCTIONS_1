# # LAB_FUNCTIONS_1


# ## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):


num = 5
def patter(num):
  for n in range(num, 0,-1):
    for j in range(n, 0,-1):
        print(j, end=" ")
    print('\r')
    
patter(num)
# 5 4 3 2 1   
# 4 3 2 1   
# 3 2 1   
# 2 1   
# 1

# ### Document the newly created function. describe what it does, then print the documentation. 
