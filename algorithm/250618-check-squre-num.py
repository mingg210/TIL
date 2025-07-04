# 문제: 어떤 자연수가 제곱수인지 판별하는 함수
# 조건:
# - n이 제곱수면 1 반환
# - 제곱수가 아니면 2 반환

def solution(n):
    root = n ** 0.5
    if int(root) == root:
        return 1
    else:
        return 2

# 예제 출력
if __name__ == "__main__":
    print(solution(144))  # 출력: 1
    print(solution(976))  # 출력: 2

