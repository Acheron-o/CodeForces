def maximum_value(a,b,c):
    results = []
    operations = [a + b * c,
                  a * (b + c),
                  a * b * c,
                  a + b + c,
                  a * b + c,
                  (a + b) * c]
    return max(operations)
a = int(input())
b = int(input())
c = int(input())
print(maximum_value(a,b,c))    