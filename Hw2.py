'''
for i in range(0, 6):
    for j in range(1, i * 2 + 2):
        print("1", end = "")
    print()
'''
for i in range(1, 10, 2):
    msg = ""
    for a in range(i):
        msg += "1"
    print("{:^9}".format(msg))
