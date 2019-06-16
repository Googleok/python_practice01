# 문제10 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
# a. 입력 받은 숫자가 홀수인 경우에는, 0 부터 입력 값까지 홀수의 합을 출력합니다.
# - 예제 : 입력이 7 이면 16을 출력 ( 1 + 3 + 5 + 7 = 16 )
# b. 입력 받은 숫자가 짝수인 경우에는, 0 부터 입력 값까지 짝수의 합을 출력합니다.
#     - 예제 : 입력이 10 이면 30을 출력 ( 2 + 4 + 6 + 8 + 10 = 30 )
# 실행 결과:
#
# 숫자를 입력하세요: 7
# 결과 값 : 16
#
# 숫자를 입력하세요: 10
# 결과 값 : 30
#
# 숫자를 입력하세요: 11
# 결과 값 : 36
import sys

str1 = input('숫자를 입력하세요: ')

if str1.isdigit() == False :
    print('정수가 아닙니다.')
    sys.exit(0)

number = int(str1)
s = 0
for i in range(number + 1):
    if i % 2 == 0 and number % 2 == 0:
        s += i
    elif i % 2 != 0 and number % 2 != 0:
        s += i
print(s)

for n in range(number + 1):
    if number & 0x0001 ^ n & 0x0001 == 0:
        s += n
print(s)
