import pandas as pd
import sys

a = 0
be_labeled = sys.stdin.readline()

be_labeled = be_labeled[0:-1]
try:
    data = pd.read_csv(be_labeled)
    data_new = data.drop(["Flow ID","Src IP","Src Port","Dst IP","Timestamp","Protocol","Dst Port"],axis=1)
    data_new.to_csv(be_labeled,index=0)

    # label_file_name = be_labeled[0:-4] + '_test_with_label.csv'
    label_file_name = 'file3.csv'
    with open(be_labeled,encoding='utf-8') as readfile, open(label_file_name,"a+",encoding='utf-8') as writefile:
        column = ['f'+str(i) for i in range(1, 78)]
        writefile.write(','.join(column)+'\n')
        for line in readfile:
            if a==0:
                a = a+1
                continue
            if 'Total Fwd Packet' in line:
                continue
            else:
                line = line[0:-16]  + '1\n'
                writefile.write(line)

except:
    exit()






