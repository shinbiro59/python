print("비만도 계산하기")
print()
print("비만도는 체중 / 신장 (제곱) 입니다")
weight=int(input("체중을 입력해주세요=> "))
cm=float(input("신장을 입력해주세요\n키는 m단위로 적어주세요 =>"))

bmi=print(weight/(cm*cm))

if (float(bmi) > 18.5):
    print("저체중입니다.")
elif (18.5<= bmi <23):
    print("정상입니다")
elif (23 <= bmi <25):
    print("과제중입니다.")
elif (25<= bmi < 30):
    print("비만입니다.")
else:
    print("고도비만입니다.")

    


