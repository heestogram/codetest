def solution(data, ext, val_ext, sort_by):
    answer = []
    dic={'code':0,'date':1,'maximum':2,'remain':3}
    extidx = dic[ext]
    sortidx = dic[sort_by]
    for da in data:
        if da[extidx]<val_ext:
            answer.append(da)
            
    answer.sort(key=lambda x: x[sortidx])
    return answer