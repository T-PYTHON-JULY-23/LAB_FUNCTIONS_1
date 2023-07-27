def pattern(nums): 
    ''' Decrease each time unit it reaches 1 '''
    result = ""
    for n1 in range(nums, 0, -1):
        for n2 in range(n1, 0, -1):
            result += f"{n2} "
        result += "\n"
    return result

pattern_output = pattern(5)
print(pattern_output)