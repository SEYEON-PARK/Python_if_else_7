score=float((input("당신의 점수를 입력해주세요. : ")))

if(score>=95):
    print("당신의 등급은 A+입니다.")
elif(score>=90):
    print("당신의 등급은 A입니다.")
elif(score>=85):
    print("당신의 등급은 B+입니다.")
elif(score>=80):
    print("당신의 등급은 B입니다.")
elif(score>=75):
    print("당신의 등급은 C+입니다.")
elif(score>=70):
    print("당신의 등급은 C입니다.")
else:
    print("아쉽습니다. 재수강하셔야 합니다.")