# 문제: 세 변의 길이가 담긴 배열 sides가 주어질 때,
#       세 변으로 삼각형을 만들 수 있으면 1, 만들 수 없으면 2를 반환하기
# 조건:
# - 삼각형 조건: 가장 긴 변 < 다른 두 변의 합
# - sides 배열 길이 = 3
# - 각 원소는 자연수, 1 ≤ 원소 ≤ 1,000
#
# 예제:
# input: [1, 2, 3] → output: 2
# input: [199, 72, 222] → output: 1

def solution(sides):
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        return 1
    else:
        return 2

if __name__ == "__main__":
    print(solution([1, 2, 3]))      
    print(solution([199, 72, 222]))
