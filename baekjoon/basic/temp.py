datas = []
result = [0 for i in range(10)]
for i in range(3):
  datas.append(input())
d = str(int(datas[0])* int(datas[1]) * int(datas[2]))
datas.append(d)

# print(result)

for i in range(len(d)):
  # print(data[i])
  result[int(d[i])] += 1
  # print(f"result[{data[i]}] : ", result[int(data[i])])

for v in result:
  print(v)




