def fib(n):
    num1 = 0
    num2 = 1
    sum = 0
    if(n >= 1):
        sum = 1
        num3 = 1
        while(num3 <= n):
            num3 = num2 + num1
            sum += num3
            num1 = num2
            num2 = num3
    return sum
