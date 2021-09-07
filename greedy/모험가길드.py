# 첫째 줄에 모험가의 수 N이 주어진다 (1 <= N <= 100,000)

# 둘째 줄에 각 모험가의 공포도 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다.

# 출력조건 : 여행을 떠날 수 있는 그룹 수의 최대값을 출력

import math

n = int(input())
gongpo = sorted(list(map(int, input().split())))
result = 0
idx = 0

while idx < n:
  x = gongpo[idx]
  if n < x:
    break

  n -= x
  idx += x
  result += 1

print(result)
