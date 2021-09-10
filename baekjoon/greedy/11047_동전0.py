# https://www.acmicpc.net/problem/11047

# 동전은 총 N 종류
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들때 동전개수의 최솟값

n, k = map(int, input().split())
sizes = []
result = 0

for i in range(n):
  sizes.append(int(input()))

for size in list(reversed(sizes)):
  result += k // size
  k %= size

print(result) 
