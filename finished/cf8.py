matrix = []
i = -1
for i in range(5):
    matrix.append(list(map(int,input().split(" "))))
  
st_idx = 0
nd_idx = 0
one_idx = []
btfl_idx = [2,2]
found = False
for i in range(len(matrix)):
    for k in range(len(matrix)):
        if matrix[i][k] == 1:
            one_idx.append(i) #The line of the matrix
            one_idx.append(k) #The column of the matrix
            found = True
            break
    if found:
        break    
    k = 0
min_steps_list = []
min_steps_list.append(abs(one_idx[0] - btfl_idx[0]))
min_steps_list.append(abs(one_idx[1] - btfl_idx[1]))
min_steps = sum(min_steps_list)
print(min_steps)
