# 문자열과 숫자의 덧셈 차이
one = '10'
two = '1'
print(one + two)

int1 = 10
int2 = 1
print(int1 + int2)

str_add = one + two
int_add = int1 + int2

print(str_add == int_add)



# dir 활용
str_te = 'cat,dog,horse'
print(type(str_te))
print(dir(str_te))                  # str_te의 유형(문자열)과 관련된 함수 목록 출력
print(str_te)

str_te_split = str_te.split(',')    # 쉼표를 기준으로 문자열을 쪼개는 함수 사용
print(type(str_te_split))
print(dir(str_te_split))            # str_te_split의 유형(리스트)과 관련된 함수 목록 출력
print(str_te_split)

# 리스트를 역순으로 만들고 출력
str_te_split.reverse()
print(str_te_split)

# 리스트를 정렬해서 출력
str_te_split.sort()
print(str_te_split)