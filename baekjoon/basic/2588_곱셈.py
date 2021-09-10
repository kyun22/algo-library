a = int(input())
b = input()
result = 0

for i in reversed(range(len(b))):
  tmp = a * int(b[i])
  print(tmp)
  result += tmp * (10 ** (2 - i))

print(result)