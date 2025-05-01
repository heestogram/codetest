import sys

n = int(input())

switch = list(map(int, sys.stdin.readline().split()))

p = int(input())

students = []
for i in range(p):
    students.append(list(map(int, sys.stdin.readline().split())))

for stud in students:
    if stud[0]==1:
        for i in range(stud[1]-1,n,stud[1]):
            switch[i]=abs(switch[i]-1)

    else:
        count=1
        num = stud[1]-1
        switch[num]=abs(switch[num]-1)

        while num-count>=0 and num+count<n and switch[num-count]==switch[num+count]:
            switch[num-count]=abs(switch[num-count]-1)
            switch[num+count]=abs(switch[num+count]-1)
            count+=1

for i in range(n):
    print(switch[i], end=" ")
    if (i+1)%20==0:
        print()
print()