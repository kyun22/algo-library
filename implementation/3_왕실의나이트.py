# 입력 조건 :  첫째줄에 8*8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다. ex)a1 열과 행

# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오
# 좌/우 로 2칸 위로 1칸, 아래로 1칸
# 위/아래 로 2칸 좌로 1칸, 우로 1칸

input_data = input()
row = int(input_data[1])
# ord : 아스키코드로 변환
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 리스트를 이용해서 각 방향에 대한 방향벡터를 정의
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2) ]

result = 0

for step in steps:
  #이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]

  # 해당 위치로 이동이 가능하면 카운트 증가
  if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <=8:
    result += 1

print(result)



