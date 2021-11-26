import sys
a = 0
with open(sys.argv[1],"r+",encoding='utf-8') as csv , open(sys.argv[2],"a+",encoding='utf-8') as total:
    for line in csv:
        if a == 0:
            a = a+1
            continue
        elif a <= sys.argv[3]:
            total.write(line)








