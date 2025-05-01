import sys

mo = ['a','e','i','o','u']

while True:
    word = sys.stdin.readline().rstrip()

    if word == "end":
        break

    word = list(word)

    if word[0] not in mo:
        mocount=1
    else:
        mocount=0

    ducount = 1

    if len(word)==1:
        if mocount==1:
            print(f"<{''.join(word)}> is not acceptable.")
        else:
            print(f"<{''.join(word)}> is acceptable.")

    else:
        for i in range(1,len(word)):
            if word[i] not in mo:
                mocount+=1
                if word[i-1] in mo:
                    ducount=1
                else:
                    ducount+=1
            else:
                if word[i-1] not in mo:
                    ducount=1
                else: ducount+=1
            if word[i-1]==word[i] and word[i]!="o" and word[i]!="e":
                print(f"<{''.join(word)}> is not acceptable.")
                break
            if ducount == 3:
                print(f"<{''.join(word)}> is not acceptable.")
                break
        
            if i == len(word)-1:
                if mocount == len(word):
                    print(f"<{''.join(word)}> is not acceptable.")

                else:
                    print(f"<{''.join(word)}> is acceptable.")
