'''
請寫一因數分解程式?
若輸入 720 執行後:
720 = 2 x 2 x 2 x 2 x 3 x 3 x 5

'''

number = int(input("輸入數字:"))

i = 2
tmp = 0
while i % number != 0:
    if number % i == 0:
        print(i,end="")
        number = number / i
        print("x", end="")
    else:
        i += 1

print(int(number))
