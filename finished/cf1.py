def is_an_even_pair(w): #They must be even as a pair of evens, they don't need to be equal.
    math = w -2
    return math != 0 and math%2 == 0
w = int(input())
if is_an_even_pair(w):
    print("YES")
else:
    print("NO")       