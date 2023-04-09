#  大樂透對獎
'''
1.電腦開出 1~49之間6個號碼(不重複)
2.使用者可以下注?自行決定幾注 由使用者輸入
3.1~49, 6個不得重複
4.對獎, 顯示中了多少注(兩個號碼即中獎)
'''

# 隨機生成6個數
import random


jackpot = random.sample(range(1, 40), 6)        # random.sample亂數生成且不重覆, 並以List回傳

# print(jackpot)                                # 顯示電腦選號的結果

setPlay = int(input('要下多少組號碼?'))
cnt = 1

setList2 = []       # 二維陣列


while cnt <= setPlay:                           
    setList = []
    tmp = 0
    print("第%d組號碼:" % (cnt))
# 選擇6個號碼,如果選擇的號碼不在裡面或者是有輸入重覆不會帶進去setList裡面並且pop出去
    while tmp < 6:
        
        choose = int(input())
        
        if choose > 49 or choose < 1:
            print("不得超過1~49或不得重複")
            
        else:
            setList.append(choose)
            
            if setList.count(choose) > 1:           
                print("數字有重複, 請重新輸入!!!")
                setList.pop()                       # 輸入該數字已經存在並且pop()出去
            else:
                tmp += 1
    setList2.append(setList)                        # 塞入setList2裡面且變成二維串列
    cnt += 1

# print(setList2)             # 印出setList2裡面的值

many = 0                        #總共中了幾注
for i in setList2:      
    tmp = 0
    for k in i:                 
        if k in jackpot:        # k去讀取setList裡面的各號碼，與jackpot[]裡的號碼配對
            tmp += 1
    if tmp >= 2:                # 規則如提中了兩個號碼中獎, many + 1
        many += 1    

        
print("恭喜中了%d注" % (many))