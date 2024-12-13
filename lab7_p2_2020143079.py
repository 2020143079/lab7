import re

with open('input_7_2.txt') as file:
    lines = file.readlines()

# alpha_counting 딕셔너리  초기화
alpha_counting={}

# 알파벳 갯수를 alpha_counting 에 저장 
for line in lines:
    alpha_lst = re.findall(r'[a-zA-Z]', line)
    for i in alpha_lst:
        if i.upper() not in alpha_counting:
            alpha_counting[i.upper()]=1
        else:
            alpha_counting[i.upper()]+=1


# alhpa_counting의 items()를 리스트로 변환
alpha_items = list(alpha_counting.items())

# sort() 메서드를 사용하여 value 기준으로 내림차순 정렬
alpha_items.sort(key=lambda x: x[1], reverse=True)

# 알파벳만 리스트로 추출

sorted_keys = []
for i in alpha_items:
    sorted_keys.append(i[0])

# 결과 출력
print(sorted_keys)
