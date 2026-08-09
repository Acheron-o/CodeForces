first_str = list(input().lower())
second_str = list(input().lower())
#==================================
def string_counter(first_str,second_str):
    rtrn = ""
    for i in range(len(first_str)):
        first_str[i] = ord(first_str[i])
        second_str[i] = ord(second_str[i])
        if first_str[i] < second_str[i]:
            rtrn = "-1"
            break
        elif second_str[i] < first_str[i]:
            rtrn = "1"
            break
    if rtrn == "":
        rtrn = "0"
    return print(rtrn)  

string_counter(first_str,second_str)