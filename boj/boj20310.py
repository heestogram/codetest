s = list(input())

count1 = s.count("1")
count0 = s.count("0")

max0 = 0
max1 = 0

new_s = ""
for item in s:
    if item == "0":
        if max0 < int(count0/2):
            max0+=1
            new_s+=item
            
    else:
        if max1 < int(count1/2):
            max1+=1
        else:
            new_s+=item

print(new_s)