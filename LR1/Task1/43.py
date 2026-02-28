a = input()
b = int(input())
c = float(input())
d = [a, b, c]
for i in d:
    for name, value in list(globals().items()):
      if value is i and name in ['a', 'b', 'c']:
        print(f"Змінна {name} має значення \"{i}\", тип {type(i)}")
        break