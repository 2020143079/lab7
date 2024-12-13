import re

# 파일 읽기
with open('input_7_1.txt') as file:
    lines = file.readlines()

# 함수 선언을 저장할 딕셔너리
functions = {}

# 첫 번째 루프: 함수 선언 찾기
for index, line in enumerate(lines, start=1):
    match = re.search(r'\s*def\s+([a-zA-Z_]\w*)\s*\(', line)
    if match:
        funcName = match.group(1)
        functions[funcName] = {'declaration': index, 'calls': []}

# 두 번째 루프: 함수 호출 찾기
for index, line in enumerate(lines, start=1):
    call_matches = re.findall(r'\b([a-zA-Z_]\w*)\s*\(', line)
    for call in call_matches:
        if call in functions and index != functions[call]['declaration'] and index not in functions[call]['calls']:
            functions[call]['calls'].append(index)

# 결과 출력
for func, data in functions.items():
    print(f"{func}: def in {data['declaration']}, calls in {data['calls']}")
