def team_solutions(n):
    solutions = 0
    while n > 0:
        found = 0
        problems = list(map(int, input().split()))
        for i in problems:
            if i == 1:
                found += 1
            if found == 2:
                solutions += 1
                found = 0
        n -= 1        
    print(solutions)
#calling the function
n = int(input())
team_solutions(n)                    
