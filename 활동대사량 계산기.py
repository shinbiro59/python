print("활동 대사량을 구해봅시다.")
print()
rlch = input("기초대사량을 입력해주세요 = >")
print("활동이 적거나 운동을 안할 경우 = 1\n가벼운 활동 및 운동(1~3/주)을 하는 경우 = 2\n보통의 활동 및 운동(3~5일/주)을 하는 경우 = 3\n적극적인 활동 및 운동(6~7일/주)을 하는 경우 = 4\n매우 적극적인 활동 및 운동 선수인 경우 = 5")
ex=input("각 각의 맞는 숫자를 적어주세요 =>")
if (int(ex) == 1):
    aa = rlch * 0.2
    print(float((aa))
elif (ex == 2):
    aa = rlch * 0.375
    print(float((aa))
elif (ex == 3):
    aa = rlch * 0.555
    print(float((aa))
elif (ex == 4):
    aa = rlch * 0.725
    print(float((aa))
else:
    aa = rlch * 0.9
    print(float((aa))
