'''
題目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一個數字。例如2+22+222+2222+22222(此時共有5個數相加)，幾個數相加由鍵盤控制。
程序分析：關鍵是計算出每一項的值。

'''

a = int(input("輸入一個數字:"))
n = int(input('要輸入幾層:'))
list_sum = list()
tmp = 1
total = 0
cnt = 0
for i in range(n):

    for j in range(i+1):
        while cnt <= j:
            if j == 0:
                total += a
                cnt += 1
                list_sum.append(total)
            else:
                for zero in range(j):
                    tmp *= 10
                total += (a * tmp)
                cnt +=1
                tmp = 1
                list_sum.append(total)

print(sum(list_sum))

