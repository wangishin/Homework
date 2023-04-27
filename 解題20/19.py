'''
19. 題目：一個數如果恰好等於它的因子之和，這個數就稱為"完數"。例如6=1＋2＋3.編程找出1000以內的所有完數。


'''
i = 2
for i in range(1001):
    list_n = list()
    number = 1
    total = 0
    while number <= i:
        if i % number == 0:
            # print(number, end=' ')
            list_n.append(number)
            number += 1
        else:
            number += 1
    if i != 0:

        for y in list_n:
            total += y
        mines_last_num = total - list_n[-1]
        if mines_last_num  == list_n[-1]:
            print(i, '是完全數')


