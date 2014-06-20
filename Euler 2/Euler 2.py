__author__ = 'eddie'

def fibo(n):
    # finding Fibonacci number > n
    sum = 0
    a, b= 0 , 1 # dual assignment in python: a , b = b , a will work
    c = a + b   # a, b, c = 0, 1, a + b will not work though
    while c < n:
        if c % 2 == 0:
            sum = sum + c
        """a, b, c = b, c, a + b""" #This statement is valid, but wrong. C is intially old a + old b
        a, b = b , c
        c = a + b

    return sum

print fibo(4000000)

[]