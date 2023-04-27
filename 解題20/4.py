'''
題目：輸入某年某月某日，判斷這一天是這一年的第幾天？
每個月分加起來去算, 判斷閏年方法:被4 100 400整除
'''

year = int(input("請輸入年:"))
month = int(input("請輸入月:"))
day = int(input("請輸入日:"))
totalDays = 0

is_leap = False
# months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month - 1):
    totalDays += days[i]

totalDays += day
# print("你輸入的%d月總計有%d天" % (month, totalDays))

if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
    is_leap = True
    leap = 1

if month > 2 and is_leap is True:
    totalDays += leap

print("你輸入的%d年%d月%d日總計有%d天" % (year, month, day, totalDays))
if is_leap:
    print("這一年是閏年%d" % year)
