# 입력조건 : 첫재 줄에 정수 N이 입력됩니다. (0 <= N <= 23)

# 출력조건 : 00시 00분 00초 부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력

n = int(input())

hour = range(n + 1)
minute = range(60)
second = range(60)
count = 0
# list_corr = [3, 13, 23, 33, 43, 53, 30, 31, 32, 34, 35, 36, 37, 38, 39]

for h in hour:
  for m in minute:
    for s in second:
      # if h in list_corr or m in list_corr or s in list_corr:
      if '3' in str(h) + str(m) + str(s):
        count += 1

print(count)