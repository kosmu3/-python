import random

number = random.randint(1,31) # 1에서 31까지 숫자중 랜덤설정
print(f' 내 마음속 숫자: {number}') # print
running = True #running = True를 설정으로 해서 정답(False)이 나올때까지 안멈추게 하기


while running:
    guess = int(input('1-31 중 내가 생각한 숫자는?')) # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
    print(f'입력받은 숫자 : {guess}') # print
    if guess < number: # if를 통해 guess < number 제시
        print('내가 생각한 숫자보다 작습니다.') # print 입력문 설정
    elif guess > number: # if를 제외한 선택지를 통해 guess > number
        print('내가 생각한 숫자보다 큽니다.') # 입력문 설정
    else: # if, elif도 아닌 나머지
        print('정답입니다.') # 입력문 설정
        running = False # 시작할때 running = True 입력해서 계속 돌아가고 있으므로 정답이 나오면 false로 설정을 해서 끝

