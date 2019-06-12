# 문제5. 주어진 리스트 데이터를 이용하여
# 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

numbers = [12, 3, 5, 6, 7, 8, 9]
add = 0
count = 0
print(len(numbers))
for i in range(0, len(numbers)):
    if numbers[i] % 3 == 0:
        add += numbers[i]
        count += 1
print('count=', count)
print('add=', add)