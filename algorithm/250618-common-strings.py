# 문제: 두 문자열 배열의 공통 원소 개수 구하기
# 조건:
# - s1, s2 배열이 주어짐
# - 두 배열 모두 중복된 원소 없음
# - 공통된 문자열의 개수를 반환
#
# 예제:
# input: ["a", "b", "c"], ["com", "b", "d", "p", "c"] → output: 2
# input: ["n", "omg"], ["m", "dot"] → output: 0

def solution(s1, s2):
    return len(set(s1) & set(s2))

# 예제 출력
if __name__ == "__main__":
    print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))  # 2
    print(solution(["n", "omg"], ["m", "dot"]))                    # 0

