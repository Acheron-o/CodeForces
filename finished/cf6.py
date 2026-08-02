def who_advances(rst_line,nd_line):
    #declaring the variables
    n = rst_line[0] #Total number of participants
    k = rst_line[1] #The number of k-th position thath will advance
    n_of_advancements = 0 #Loop that will check whenever the number of participants must be frozen
    if nd_line[0] == 0:
        return n_of_advancements #The score must be > 0 , so in this scenario none of them pass
    if n == k: #If the number of k-th positions is equal to the number of participants
        n_of_advancements += n - nd_line.count(0) #If they are equal, but there are also some zeros there
        return n_of_advancements
    #If the scenario is valid, the evaluation continues
    else:
        #It will count the number of advancements as long as the n-th position is not equal to k-th postion
        for i in range(k + 1):
            if nd_line[i] == 0: #The k-th position could hold a 0 score, thus it must not pass
                break
            elif i == k: #If it pass, it would work as usual
                break
            else:
                n_of_advancements += 1
        #Create another variable, that saves the position where the last loop started
        idx = k  
        #However if not, it will count until a tie is not possible between the k-th participants beyond the limits imposed by the system     
        while nd_line[idx] == nd_line[k - 1] and nd_line[idx] != 0: #It also checks if someone scored 0 at some
            n_of_advancements += 1
            idx += 1   
            if idx == n:
                break
                    
    return n_of_advancements
#user inputs
rst_line = list(map(int,input().split(" ")))
nd_line = list(map(int,input().split(" ")))
#calling the function
print(who_advances(rst_line,nd_line))
    

