def paradaigm(num:int) -> None:
    '''this function will draw a upside down paradigm with the size you give to it'''
    i = num
    while num != 0:
        line = ""
        while i > 0:
            line = line + "{} ".format(i)
            i = i - 1
        print(line)
        num = num - 1 
        i = num
        

paradaigm(5)
print(paradaigm.__doc__)