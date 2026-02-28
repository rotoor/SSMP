a = input()
b = int(input())
c = float(input())
d = [a, b, c]
for i in d:
    for name, value in list(globals().items()):
      if value is i and name in ['a', 'b', 'c']:
        typename = type(i)
        print(f"Змінна %s має значення \"%s\", тип %s" % (name, i, typename))
        break