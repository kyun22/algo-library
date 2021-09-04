# Greedy - 거스름돈 동전 최소 개수

n = 1280
count = 0
array = [500, 100, 50, 10]

for coin in array:
  count += n // coin
  n %= coin

print(count)