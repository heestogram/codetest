from collections import defaultdict,Counter
def solution(points, routes):
    crash = 0
    info=[]
    def bfs(start,target,time,first,info):
        
        x,y=start[0]-1,start[1]-1
        target_x,target_y=target[0]-1,target[1]-1
        if first:
            info.append((time,(x,y)))
        if x>target_x:
            while x>target_x:
                time+=1
                x-=1
                info.append((time,(x,y)))
        elif x<target_x:
            while x<target_x:
                time+=1
                x+=1
                info.append((time,(x,y)))
        if y>target_y:
            while y>target_y:
                time+=1
                y-=1
                info.append((time,(x,y)))
        elif y<target_y:
            while y<target_y:
                time+=1
                y+=1
                info.append((time,(x,y)))
        return time, info
    
    crash=0
    for ro in routes:
        time=0
        for i in range(len(ro)-1):
            if i>0:
                first=False
            else:
                first=True
            time,info= bfs(points[ro[i]-1], points[ro[i+1]-1], time, first, info)

    dic=defaultdict(list)
                            
    for i in info:
        dic[i[0]].append(i[1])
        
    for i in list(dic.values()):
        freq = Counter(i)
        for j in list(freq.values()):
            if j>=2:
                crash+=1
        
    return crash