def solution(schedules, timelogs, startday):
    answer = 0
    deadline=[]
    for s in schedules:
        if 50<=(s%100)<=59:
            deadline.append(s+50)
        else:
            deadline.append(s+10)
    for i in range(len(schedules)):
        today = startday
        cnt=0
        for j in range(7):
            if today in (1,2,3,4,5):
                if timelogs[i][j]<=deadline[i]:
                    cnt+=1
            if today==7:
                today=1
            else:
                today+=1
        if cnt==5:
            answer+=1

    return answer