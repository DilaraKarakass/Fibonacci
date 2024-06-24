def Fibonacci(number):
    if number<0:
        return -1
    elif number==0:
        return [0]
    elif number==1:
        return [0,1]
    else :
        fibonacci=[0,1]
        for i in range(2,number):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        return fibonacci    

print(Fibonacci(3))