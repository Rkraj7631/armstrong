def is_armstrong(n):
    original=n
    sum=0
    power=len(str(n))
    while n>0:
        digit=n%10
        sum+=digit**power
        n=n//10

    if original==sum:
        return "armstorng"
    else:
        return "not armstrong"
print(is_armstrong(407))
    
