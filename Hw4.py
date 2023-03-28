a = int(input("輸入第一個值"))
b = int(input("輸入第二個值"))
c = int(input("輸入第三個值"))


if a + b > c and a + c > b and a + c > b:
    print("可構成三角形")
elif a == b == c:
    print("正三角形")
elif a == b or a == c or b == c:
    print('等腰三角形')
else:
    print("不是三角形")