data = [
[100,100,100,100],
[100,110,100,110],
[100,120,100,120],
[100,120,100,115],
[100,130,100,130],
[100,140,100,140],
[100,140,100,125],
[100,140,100,100],
[100,140,95,95],
[100,140,85,85],
[100,140,85,135],
[100,145,85,145],
[100,145,50,50],
[100,145,50,75]
]

   # data 변수에 데이터 집합을 저장
data.append(0) # 배열[마지막]:종목 예외 시 검증 변수 추가
#---------------------------------------------------------


for num in range(len(data)-1):                                                   
    op_hi_per = float((data[num][1]-data[num][0]) / data[num][0]) * 100 # 시_고(100분율) 
    op_cl_per = float((data[num][3]-data[num][0]) / data[num][0]) * 100 # 시_종(100분율)
    hi_cl_per = float((data[num][3]-data[num][1]) / data[num][1]) * 100 # 고_종(100분율)
    print_per = data[num].append([op_hi_per,op_cl_per,round(hi_cl_per)])# 배열[num][4]: 시_고, 시_종, (고_종(round함수로 소수점 제한)) 
    # pi_lv = data[num].append(0)                                         # 배열[num][5]:피라미딩 값 추가
   

    if op_hi_per > 5 and hi_cl_per > -5 and data[len(data)-1] == 0 :
        
        print("Buy",data[num])
        
    elif hi_cl_per < -5 and  data[len(data)-1] == 0 :
        data[len(data)-1] = 1
        print("Sell",data[num])

    elif data[len(data)-1] == 1:
        print("Except_reise", data[num])

    else: 
        print("No,Action",data[num])
        
        
        
