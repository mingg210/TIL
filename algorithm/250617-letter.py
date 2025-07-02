# 문제: 할머니께 편지를 쓰기 위해 필요한 최소 가로길이 계산하기
# 조건:
# - 한 글자당 가로 길이 2cm
# - message의 길이는 최대 50
#
# 예제:
# input: "I love you~" → output: 22

def solution(message):
    return len(message) * 2

# 예시 출력
if __name__ == "__main__":
    print(solution("I love you~"))      # 22
