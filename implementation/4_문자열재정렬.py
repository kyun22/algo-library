# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어짐.abs

# 알파벳을 오름차순으로 정렬하여 이어서 출력한 후에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력

###########################################################

# input_data = input()
# sorted_data = sorted(input_data)
# string_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# index_char = 0
# result = 0

# for c in sorted_data:
#   if c in string_number:
#     index_char += 1
#   else:
#     break

# int_data = sorted_data[:index_char]
# string_data = sorted_data[index_char:]

# for x in int_data:
#   result += int(x)
# print(''.join(string_data) + str(result))

###########################################################

data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
  # 알파벳인 경우 결과 리스트에 삽입
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

# 알파벳을 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하면 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

print(''.join(result))
