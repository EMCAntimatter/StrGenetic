x = 1
try:
    while True:
        x = x * 2
        print(x)
        chr(x)
except ValueError:
    print(x-1)


