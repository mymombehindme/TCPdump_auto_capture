import sys
import io
import csv
import pandas as pd
a = 0
b = sys.stdin.readline()

b = b[0:-1]

try:
    with io.open(b,"r+",encoding='utf-8') as csvfile ,io.open('file3.csv',"a+",encoding='utf-8') as file2:  
        for line in csvfile:
            if a==0:
                file2.write(line)
                a = a+1
                continue
            if 'Total Fwd Packet' in line:
                continue
            else:
                file2.write(line)
        csvfile.close()
        file2.close()

    data = pd.read_csv('file3.csv')
    data.loc[:,['Label']] = 0

    data_new = data.drop(["Flow ID","Src IP","Src Port","Dst IP","Timestamp","Protocol"],axis=1)
    data_new.to_csv("file3.csv",index=0)

except:
    exit()

# label_file_name = be_labeled[0:-4] + '_with_label.csv'
# count = 0

# with open(be_labeled,encoding='utf-8') as readfile, open(label_file_name,"a+",encoding='utf-8') as writefile:
#     for line in readfile:
#         if a==0:
#             a = a+1
#             writefile.write(line)
#             continue
#         if 'Need' in line:
#             line = line[0:-16] + sys.argv[2] + '\n'
#             writefile.write(line)

