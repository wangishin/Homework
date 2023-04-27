'''
1.	題目：有四個數字：1、2、3、4，能組成多少個互不相同且無重複數字的三位數？各是多少？

'''
cnt = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and i != k:
                print(i, j, k)
                cnt += 1
print("共有%d個" % cnt)
