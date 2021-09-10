# 여행가 A는 N * N 크기의 정사각형 공간 위에 서있다. 가장 왼쪽 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N) 이다. 시작좌표는 항상 (1, 1)이다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 LRUD중 하나의 문자가 반복적으로 적혀있다.
# N * N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.  

# 입력조건 : 첫째 줄에 공간의 크기를 나타내는 N이 주어짐 ( 1<= N <= 100), 둘째 줄에 여행가 A가 이동할 계획서 내용 주어짐.

# 출력 조건 A가 최종적으로 도착할 지점의 좌표 (X, Y) 를 공백으로 구분하여 출력


# n = int(input())
# plan = list(input().split(sep = " "))
# x = 1
# y = 1

# for c in plan:
#   if c == 'L':
#     x -= 1
#   elif c == 'R':
#     x += 1
#   elif c == 'U':
#     y -= 1
#   elif c == 'D':
#     y += 1
  
#   if x < 1: x += 1
#   if x > n: x -= 1
#   if y < 1: y += 1
#   if y > n: y -= 1
#   print()

# print(x, y)

n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]    

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    
    x, y = nx, ny

print(x, y)