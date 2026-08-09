nickname = list(input())
found = []
def is_even(found):
    return len(found)%2 == 0
#=========================
for i in nickname:
    if i not in found:
        found.append(i)
if is_even(found):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")