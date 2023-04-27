'''
    題目：印出9*9乘法表
'''


for i in range(1, 10):
    for j in range(1, 10):
        print("%d x %d = %d " %(i, j, i * j), end="")
    print()

