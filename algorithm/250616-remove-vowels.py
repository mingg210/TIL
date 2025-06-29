# 문제: 문자열에서 모음을 제거한 결과를 반환하기
# 조건:
# - 모음은 'a', 'e', 'i', 'o', 'u' 다섯 개
# - 문자열은 소문자와 공백으로 구성됨
# - 1 ≤ 문자열 길이 ≤ 1,000
#
# 예제:
# input: "bus" → output: "bs"

def solution(my_string):
    result = ""
    for i in my_string:
        if i not in ["a", "e", "i", "o", "u"]:
            result += i
    return result

# 예시 출력
if __name__ == "__main__":
    print(solution("bus"))
