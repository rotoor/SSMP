'''for i in range(3):
    n = int(input())
    h = (n // 60) % 24
    m = n % 60
    print(h, m)
    Переплутав з 63'''
for i in range(3):
    n = int(input())
    r = hex(n)[2:]
    print("%x" % n)