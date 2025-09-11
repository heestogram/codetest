def ms(x):
    m, s = map(int,x.split(":"))
    return (m,s)

def ms_sum(x,com,video_len):
    m,s=x[0],x[1]
    if com=="next":
        if 50<=s<=59:
            s=(s+10)%60
            m+=1
        else:
            s+=10
        if m*60+s>ms(video_len)[0]*60+ms(video_len)[1]:
            m,s=ms(video_len)[0],ms(video_len)[1]
            
    elif com=="prev":
        if 0<=s<=9:
            s=60-10+s
            m-=1
        else:
            s-=10
        if m*60+s<0:
            m,s=0,0
    return (m,s)
    
            
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    now=ms(pos)
    op_s = ms(op_start)
    op_e = ms(op_end)
    for com in commands:
        if op_s[0]*60+op_s[1]<=now[0]*60+now[1]<=op_e[0]*60+op_e[1]:
            now = op_e
        now = ms_sum(now,com,video_len)
        if op_s[0]*60+op_s[1]<=now[0]*60+now[1]<=op_e[0]*60+op_e[1]:
            now = op_e
    if len(str(now[0]))==1:
        m="0"+str(now[0])
    else:
        m=str(now[0])
    if len(str(now[1]))==1:
        s="0"+str(now[1])
    else:
        s=str(now[1])
    answer=m+":"+s
    return answer