def reversed_number (num:int):
    ''' print reversed number in descending order '''
    for number in range(num,0, -1):
        for numberResult in range(number,0, -1):
            print(numberResult,end = " ")
        print ('')
        
reversed_number(7)
