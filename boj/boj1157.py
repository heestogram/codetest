word = list(input().lower())


dic = {}
for w in word:
    try:
        dic[w]+=1
    except KeyError:
        dic[w]=1

result = [k for k,v in dic.items() if max(dic.values())==v]

if len(result)>=2:
    print("?")
else:
    print(result[0].upper())