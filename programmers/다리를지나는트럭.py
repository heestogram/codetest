from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    cur_weight=0
    while truck_weights:
        answer+=1
        cur_weight-=bridge.popleft()

        if cur_weight+truck_weights[0]<=weight:
            bridge.append(truck_weights[0])
            cur_weight+=truck_weights.popleft()
        else:
            bridge.append(0)
        
    
    return answer+bridge_length