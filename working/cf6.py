def equal_counter(nd_line,k):
    counter = 0
    for i in range(len(nd_line)):
        if nd_line[i] == nd_line[k] or nd_line[i] == nd_line[i - 1]:
            counter += 1

    return len(nd_line) - counter - k        
def who_advances(rst_line,nd_line):
    #declaring the variables
    n = rst_line[0]
    k = rst_line[1]
    counter = 0
    for i in range(n):
        if nd_line[i] == 0 or equal_counter(nd_line,k) != 0:
            break
        else:
            counter += 1 
        if nd_line[i] == nd_line[k - 1] and nd_line[i + 1] != nd_line[i]:
            break
         
    return counter
#user inputs
rst_line = list(map(int,input().split(" ")))
nd_line = list(map(int,input().split(" ")))
#calling the function
print(who_advances(rst_line,nd_line))
    

