total = 0
height = 100

for i in range(10):
    total += height
    height /= 2
    total += height

    print(height)
    print(total)
