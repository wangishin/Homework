'''
5. 題目：輸入三個整數x,y,z，請把這三個數由小到大輸出。
'''


x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))


arr = list()

arr.append(x)
arr.append(y)
arr.append(z)

for i in sorted(arr):
    print(i)


