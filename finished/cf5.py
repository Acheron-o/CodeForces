def bit_plus_plus(n):
    x = 0
    operations = []
    addition = ["X++","++X"]
    subtraction = ["X--","--X"]
    while n > 0:
        statements = input()
        operations.append(statements)
        n -= 1           
    for i in operations:
        if i in addition:
            x += 1
        elif i in subtraction:
            x -= 1    
    return x        

n = int(input())
#calling the function
print(bit_plus_plus(n))    
    