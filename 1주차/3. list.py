# 리스트 선언법
a = [1,2,3,4,5]
b = [1,2,[1,2]]
c = [1,'test','tset']
d = [1,'test',['tset',1]]
a = list()  # 빈 리스트 생성하기

# 리스트는 기본적으로 c의 배열과 비슷하다.

# 리스트 인덱싱하기
a = [1,2,3]
a[0]                        # 1
a[0]+a[2]                   # 1 + 3 = 4
a[-1]                       # 3
a = [1,2,3,['a','b','c']]
a[3]                        # ['a','b','c']
a[3][1]                     # 'b'

# 리스트 자르기, 합치기, 곱하기, 길이구하기는 str와 동일하다.

# 리스트 바꾸기, str와 달리 수정이 가능한 객체이다.
a = [1,2,3]
a[2] = 4                    # [1,2,4]

# 리스트 아이템 지우기
# del 함수를 이용한다
a = [1,2,3,4,5]
del a[1]                    # [1,3,4,5]
del a[2:]                   # [1,3]

# 리스트 추가하기
a = [1,2,3]
a.append(4)                 # [1,2,3,4]
a.append([5,6])             # [1,2,3,4,[5,6]]

# 리스트 정렬하기
# 개인적으로 가장 잘만들었다고 생각하는 함수
# 리스트 안에 리스트나 다른 객체가 들어간경우 그 객체의 첫번째를 비교해서 정렬해준다.
a = [1,3,2,4]
a.sort()                    # [1,2,3,4]

# 리스트 뒤집기
a = [1,2,3]
a.reverse()                 # [3,2,1]

# 이스트 안에 있는 데이터 찾기
# 없는경우 error를 반환한다.
a = [1,2,3]
a.index(3)                  # 2
a.index(0)                  # error

# 리스트 안에 삽입하기 (insert(위치,데이터))
a = [1,2,3]
a.insert(1,4)               # [1,4,2,3]

# 리스트 데이터 지우기, 가장 첫번째로 나오는 데이터를 지웁니다.
a = [1,2,3,1,2,3]
a.remove(3)                 # [1,2,1,2,3]

# 리스트 pop, pop함수의 리턴값은 맨끝의 항목입니다.
a = [1,2,3]
a.pop()                     # 3, a = [1,2]

# 리스트 안에 있는 데이터 갯수 구하기
# 존재하지 않는 경우 0을 반환한다.
a = [1,2,1,3]
a.count(1)                  # 2

# 리스트 확장하기, 서로 다른 두 리스트를 합치는 방법
a = [1,2,3]
a.extend([4,5])             # [1,2,3,4,5] // same a += [4,5]


