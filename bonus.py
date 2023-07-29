def inverse_pyramid_with_output(number:int) -> str:
    output = ""
    for n in range(number, 0, -1):
        for n2 in range(n, 0, -1):
            output += f"{n2} "
        
        output += "\n"
        
    return output
    
    
print(inverse_pyramid_with_output(5))