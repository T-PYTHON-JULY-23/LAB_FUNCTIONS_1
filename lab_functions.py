def number(num:int ) -> int:
   '''this is Numbers sppear to me hierarchical '''
   for line in range(num,0,-1):
    for  i in range(line,0,-1):
        print( i , end="" )
    print()

print(number.__doc__)
number(5)
