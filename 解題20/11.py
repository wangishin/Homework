'''
題目：古典問題：有一對兔子，從出生後第3個月起每個月都生一對兔子，小兔子長到第三個月後每個月又生一對兔子，假如兔子都不死，問每個月的兔子總數為多少？
程序分析：兔子的規律為數列1,1,2,3,5,8,13,21....


馬的就廢是數列
'''

num = int(input("幾個月:"))

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

for i in range(num):
    print(fib(i), end=" ")