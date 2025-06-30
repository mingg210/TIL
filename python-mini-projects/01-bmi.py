# bmi.py
# This script calculates BMI (Body Mass Index) based on user input for height and weight,
# and prints out the corresponding health status. Includes error handling.

def bmi():
    try:
        height = float(input("키 입력(cm): ")) / 100
        weight = float(input("몸무게 입력(kg): "))
        bmi = weight / height ** 2
        print(f"당신의 BMI는 {bmi:.1f}입니다.")

        if bmi < 18.5:
            print("저체중입니다.")
        elif bmi < 23:
            print("정상입니다.")
        else:
            print("과체중입니다.")
    except Exception as e:
        print("잘못 입력하셨습니다.", e)
    finally:
        print("BMI 계산기를 종료합니다.")

if __name__ == "__main__":
    bmi()

