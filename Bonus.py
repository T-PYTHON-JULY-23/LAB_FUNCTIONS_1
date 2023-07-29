def numbers(x:str):
  outcome = ""   
  for i in range(x,0,-1): 
      for j in range (i,0,-1):
       outcome += f"{j} "
      outcome += "\n"
       
  return outcome
outcome = numbers
print(outcome(5))

