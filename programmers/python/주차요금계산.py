# 44m
# level 2 60%
from math import ceil
from collections import defaultdict

def time_calc(in_time, out_time):
    result = 0
    if int(in_time[3:]) <= int(out_time[3:]):
        result += 60*(int(out_time[:2]) - int(in_time[:2]))
        result += (int(out_time[3:]) - int(in_time[3:]))
    else:
        result += 60*(int(out_time[:2]) - int(in_time[:2])-1)
        result += (60-(int(in_time[3:])-int(out_time[3:])))
    return result
        

def solution(fees, records):
    time = defaultdict(list)
    for rec in records:
        t, num, _ = rec.split(" ")
        time[num].append(t)
    cars = list(time.keys())
    cars.sort()
    total_time = []
    for car in cars:
        car_list = time[car]
    
        time_rec = []
        n = len(car_list)
        even = False
        if n%2==0:
            even = True
        for i in range(0,n,2):
            if even:
                time_rec.append(time_calc(car_list[i], car_list[i+1]))
            else:
                if i == n-1:
                    time_rec.append(time_calc(car_list[i], "23:59"))
                else:
                    time_rec.append(time_calc(car_list[i], car_list[i+1]))
        answer = 0
        time_r = 0
        for t_r in time_rec:
            time_r+=t_r
            
        if (time_r-fees[0])/fees[2]<0:
            answer += fees[1]
        else:
            answer += (fees[3]*ceil((time_r-fees[0])/fees[2])+fees[1])
        total_time.append(answer)
                
        
    
            
    return total_time