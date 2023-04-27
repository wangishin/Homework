'''
題目：印出費氏數列（Fibonacci sequence），又稱黃金分割數列，指的是這樣一個數列：0、1、1、2、3、5、8、13、21、34、……。


'''


m = int(input("輸入數列:"))
def fib(n):
    output = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(m):
    print(fib(i), end='  ')