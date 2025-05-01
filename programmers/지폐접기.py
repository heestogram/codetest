def solution(wallet, bill):
    answer = 0
    bmax=max(bill)
    bmin=min(bill)
    wmax=max(wallet)
    wmin=min(wallet)
    while not(bmax<=wmax and bmin<=wmin):
        if bmax//2<bmin:
            bmax,bmin=bmin,bmax//2
        else:
            bmax=bmax//2
        answer+=1
    return answer