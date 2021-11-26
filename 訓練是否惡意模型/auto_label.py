import sys
import pandas as pd
a = 0
be_labeled = sys.argv[1]

data = pd.read_csv(be_labeled)
data_new = data.drop(["Flow ID","Src IP","Src Port","Dst IP","Timestamp","Protocol"],axis=1)
data_new.to_csv(be_labeled,index=0)

label_file_name = be_labeled[0:-4] + '_with_label.csv'
count = 0

with open(be_labeled,encoding='utf-8') as readfile, open(label_file_name,"a+",encoding='utf-8') as writefile:
    for line in readfile:
        if a==0:
            a = a+1
            writefile.write(line)
            continue
        if 'Need' in line:
            line = line[0:-16] + sys.argv[2] + '\n'
            writefile.write(line)






