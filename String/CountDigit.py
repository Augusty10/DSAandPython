def is_Countdigit(n):
    num=n
    count=0
    while num>0:
        count+=1
        num=num//10
    return count
print(is_Countdigit(5438))
