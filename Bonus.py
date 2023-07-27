def Print_number(number) :
    printNumber = ""
    for i in reversed(range(1 ,number+1)):
           for j in reversed(range(1 , i+1)):
              printNumber += f"{j }"
           printNumber += "\n"

    return printNumber

           
print (Print_number(10) )