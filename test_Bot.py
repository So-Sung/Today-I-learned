#---------------------- 임의의 변수들 설정--------------------#
j = 0
current_value = 1            #현재 가격은 그냥 임의의 값으로 나둠 
stored_value = 0          #저장된 가격
piramiding_level = [0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    i = 0

    #--------------------------변수 한번에 받고 초기화-------------#
    open_value,high_value,low_value,close_value = input("시가, 고가, 저가, 종가 순서대로 입력하기").split()
    open_value = int(open_value)
    high_value = int(high_value)
    low_value = int(low_value)
    close_value = int(close_value)
    #---------------------------변동률 변수 설정-------------------#
    open_high_rate = float((high_value - open_value) / open_value)  # 시가에서 고가 변동률
    open_close_rate = float((close_value - open_value) / open_value) # 시가에서 종가 변동률
    close_high_rate = float((high_value - close_value) / close_value) # 고가에서 종가까지 변동률
    #--------------------------변동률 테스트------------------------#
    print("open_high_rate #시가_고가 : ", open_high_rate)
    print("open_close_rate #시가_종가 : ", open_close_rate)
    print("close_high_rate #종가_고가 : ", close_high_rate)
    #---------------------------함수 구현--------------------------#
    #---------------------------매수 구현--------------------------#
    if open_high_rate > 0.05 and (close_high_rate) < 0.05:             #시가 기준 고가가 5% 이상이면서 고가대비 종가가 5% 미만일 때 
        i += 1
        if piramiding_level[i-1] < current_value:                    # 바로 직전 구매한 피라미딩 레벨의 값과 비교하여 이상 일 때만 구매    
            piramiding_level[i] = current_value                         # 현재 피라미딩 값에 구매한 가격 기록 
            current_value += 10000                                      # 현재 가격을 알 수 없어서 로직 통과를 위한 임의의 값 지정 
            stored_value += piramiding_level[i]                        # 총 매수 가격에 현재 가격 더함 
            print("매수")
            print("lv",i, ":", piramiding_level[i])
            print("총 매수 가격 :", stored_value)
        else:
            print("이미 매입")
            for i in range(11):
                print("lv", [i], ":", piramiding_level[i])

    elif piramiding_level[i] > 0 and (close_high_rate) > 0.05:              # 피라미딩 레벨이 있고, 고가 기준 종가 가격이 5%이상일 때 종료 
        break  # 반복문 탈출    
    else:
        continue
        
piramiding_level.clear()                                          # 값을 저장했던 피라미딩 레벨 초기화
print("전량 매도")                                                     
