import sys

p = int(input())



# def standing(line):
#     count = 0
#     for i in range(1,20):
#         for j in range(i+1,21):
#             if line[i]>line[j]:
#                 line[i],line[j]=line[j],line[i]
#                 count+=1

#     return count



def standing(line):
    count=0
    templine = []
    templine.append(line[1])
    for i in range(2,21):
        if line[i]>max(templine):
            templine.append(line[i])
            continue

        for j in range(0,i-1):
            if templine[j]>line[i]:
                templine.insert(j,line[i])
                count += (len(templine)-j-1)
                break

    return count


for i in range(p):

    line = list(map(int, sys.stdin.readline().split()))
    print(line[0],standing(line))