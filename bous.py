def pattern(nums:str): 
    ''' Decrease each time unit it reaches 1 '''
    result = ""
    for n1 in range(nums, 0, -1):
        for n2 in range(n1, 0, -1):
            result += f"{n2} "
        result += "\n"
    return result

pattern_output = pattern('A')
print(pattern_output)