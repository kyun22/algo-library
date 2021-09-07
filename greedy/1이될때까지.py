n, k = map(int, input().split())

result = 0

while True:
  # N이 K로 나누어지는 수
  target = n // k * k 
  # 나누어질때까지 빼야하므로 카운트
  result += (n - target)
  n = target

  if n < k:
    break;

  # 1번 나누고 다시 루프
  result += 1
  n = n // k 

# n < k 일때 1이될때까지 빼기
result += (n - 1)
print(result)
