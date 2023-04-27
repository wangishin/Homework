'''
題目：輸入一行字符，分別統計出其中英文字母、空格、數字和其它字符的個數。
程序分析：利用while或for語句,條件為輸入的字符不為'\n'。


'''


sentence = input("輸入一段文字我幫你計算有多少空格文字")
letters = 0
spaces = 0
digits = 0
others = 0
for i in sentence:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        spaces += 1
    elif i.isdigit():
        digits += 1
    else:
        others += 1

print("文字%d, 空格%d, 數字%d , 標點符號%d" % (letters, spaces, digits, others))