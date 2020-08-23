import math
def isPrime(num):
    if num < 2:
        return "Invalid value, number must be greater than 2"
    for x in range(2,num):
        print(num,"%",x,"=",num%x)
        if num%x == 0:
            return False
        else:
            continue
    return True


def isPrimeNoMod(num):
    num = float(num)
    if num < 2:
        return "Invalid value, number must be greater than 2"
    for x in range(2,int(num)):
        result = num/x
        if math.floor(result) == result:
            return False
        else:
            continue
    return True


