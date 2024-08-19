# 딕셔너리에 항목 추가 후 모든 키와 키에 대응하는 값 반환
animal_counts = {}              # 빈 딕셔너리 생성

# 딕셔너리에 항목 넣기
animal_counts['dogs'] = 5
animal_counts['cats'] = 2
animal_counts['horse'] = 1
animal_counts['snakes'] = 0

print(animal_counts.items())    # 딕셔너리에 있는 모든 아이템 보기

print(animal_counts.keys())     # 딕셔너리에 있는 모든 키 보기
print(animal_counts['dogs'])    # 딕셔너리에서 키 값이 dogs인 항목의 값 보기