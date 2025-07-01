# 문제: 문자열 배열의 각 원소 길이 구하기
# 조건: 문자열 배열 strlist가 주어질 때, 각 문자열의 길이를 담은 리스트를 반환
# 예시: ["We", "are", "the", "world!"] => [2, 3, 3, 6]

def solution(strlist):
    result = []
    for i in strlist:
        result.append(len(i))
    return result

if __name__ == "__main__":
    print(solution(["We", "are", "the", "world!"]))  # 출력: [2, 3, 3, 6]

