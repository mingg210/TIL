# 문제: 두 정수를 비교해서 같으면 1, 다르면 -1을 반환하는 함수
# 조건:
# - num1과 num2가 주어짐
# - num1 == num2 → 1 반환
# - num1 != num2 → -1 반환
#
# 예제:
# input: 2, 3 → output: -1
# input: 11, 11 → output: 1

def solution(num1, num2):
    return 1 if num1 == num2 else -1

# 예제 출력
if __name__ == "__main__":
    print(solution(2, 3))   # -1
    print(solution(11, 11)) # 1

