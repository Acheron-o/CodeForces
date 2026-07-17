def abbreviation(n):
    words = []
    while n > 0:
       word_input = input()
       if len(word_input) > 10:
           word_input = word_input[0] + f"{len(word_input) - 2}" + word_input[len(word_input) - 1]
           #print
           print(word_input)
       else:   
           #print
           print(word_input)
       n -= 1       
    for i in words:
        print(i)

n = int(input())     
abbreviation(n)          