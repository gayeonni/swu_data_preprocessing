# 코드의 기본 실행 순서 : 위에서 아래로
# 예시 - 다양한 유형의 값을 갖는 딕셔너리
cat_names = ['Walter', 'Ra']
dog_names = ['Joker', 'Simon', 'Ellie']
horse_names = ['Mr.Ed']

animal_counts_integer = {'cats': 2, 'dogs': 3, 'horse': 1}

animal_count_list = {
'cats': ['Walter', 'Ra'],
'dogs': ['Joker', 'Simon', 'Ellie'],
'horses': ['Mr.Ed']
}

animal_counts_variable = {'cats': cat_names, 'dogs': dog_names, 'horses': horse_names}

print(animal_counts_integer)
print(animal_count_list)
print(animal_counts_variable)


# 두 변수의 타입, 값이 같은지 알아보기
str_te = '10'
int_te = 10

if type(str_te) == type(int_te):
    print('두 변수의 유형은 같습니다.')
elif int(str_te) == int_te:
    print('두 변수의 값은 같습니다.')
else:
    print('두 변수의 유형과 값은 다릅니다.')
