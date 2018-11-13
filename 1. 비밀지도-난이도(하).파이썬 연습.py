'''
1. 예제 문제 : 비밀지도 (난이도 : 하)
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다.
그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다.
다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 “공백”(“ “) 또는 “벽”(“#”) 두 종류로 이루어져 있다.
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 “지도 1”과 “지도 2”라고 하자.
지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다.
지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.“지도 1”과 “지도 2”는 각각 정수 배열로 암호화되어 있다.
암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

출처 : http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
'''

# 참조 CODE 1
def my1(n, arr1, arr2):
    if n<1 or n>16 :
        print("Out of range!")
        return None
    print(["{0:b}".format( (i|j)).zfill(n).replace('0', " ").replace('1', '#')
            for i, j in zip(arr1,arr2)])

# my1(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

# 참조 CODE 2
def secret(n, arr1, arr2):
    print(['{0:b}'.format((i | j)).zfill(n).replace('0', ' ').replace('1', '#') for i, j in zip(arr1, arr2)])

# 실행 확인
# secret(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

# 참조 CODE 3
def secret_map(n, arr1, arr2):
    for i in range(n):
        row = bin(arr1[i] | arr2[i])
        row = row[2:]
        row = row.zfill(n)
        row = row.replace('0', ' ')
        row = row.replace('1', '#')
        print(row)

#실행 확인
#secret_map(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])

# 변형
def aa(n, arr1, arr2):
    for i in range(0,n):
        a = bin(arr1[i] | arr2[i])[2:].zfill(n).replace('0',' ').replace('1', '#')
        print(a)

# aa(6, [1,58, 28, 18, 11,63], [30, 1, 21, 17, 28, 63])

# 내 CODE -1
def my2(n, arr1, arr2):
    if n<1 or n>16 :
        print("Out of range!")
        return None
    arr=[]
    total=list(zip(arr1,arr2))
    for i in range(0,n):
        add= bin(total[i][0] | total[i][1])[2:].zfill(n).replace('0',' ').replace('1','#')
        arr.append(add)
    print(arr)

# 실행 확인
# my2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
# my2(n=6, arr1=[46, 33, 33 ,22, 31, 0], arr2=[27 ,56, 19, 14, 14, 0])
# my2(n=7, arr1=[46, 33, 33 ,22, 31, 50, 31], arr2=[27,56, 19, 14, 14, 10, 31])

# 내 CODE - 2
def my2(n, arr1, arr2):
    if n<1 or n>16 :
        print("Out of range!")
        return None
    arr=[]
    total=list(zip(arr1,arr2))
    for i in range(0,n):
        add= '{0:b}'.format(total[i][0] | total[i][1]).zfill(n).replace('0',' ').replace('1','#')
        arr.append(add)
    return arr

# 실행 확인
# print( my2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) )

#관련 메써드

# bin()함수 - 10진수를 2진수 문자열로 변환
# print( bin(10)) : 0b1010
# print(int('0b1010',2)) : 2진법 10진법으로 바꾸기

#oct()함수 - 10진수를 8진수 문자열로 변환
#hex()함수 - 10진수를 16진수 문자열로 변환

#10진법(ex)숫자 10)을 2진법으로 바꿀 때 사용한 방법 2가지
#1 : '{0:b}'.format(10) => 1010
#2 : bin(10)[2:] => 1010


