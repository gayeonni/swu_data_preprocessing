# string 더하기
str_1 = 'Hello'
str_2 = 'world'

print(str_1 + str_2)        # first trial : 공백이 없다
print(str_1 + ' ' + str_2)  # second trial : 강제로 공백 삽입
print(str_1, str_2)         # third trial : print() 함수의 쉼표 기능 사용

# 리스트 더하기
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_1 + list_2)


# 리스트에서 항목 추가 및 제거
dog_names = []
print(dog_names)

dog_names.append('Joker')  # 리스트에 항목 추가
dog_names.append('Ellie')  # 리스트에 항목 추가
dog_names.append('Walker') # 리스트에 항목 추가
dog_names.append('Walker') # 리스트에 항목 추가
print(dog_names)

dog_names.remove('Walker') # 리스트에서 항목 제거 / 모두 제거하는게 아닌 하나만 제거한다
print(dog_names)