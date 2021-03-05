#by Max
def get_sum(a,b):
    if(b < a): 
        temp = a
        a = b
        b = temp
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum
