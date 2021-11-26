import csv
import pandas as pd
import sys
be_droped = sys.argv[1]
new_csv = be_droped[0:-4] + "_attack_type.csv"
data = pd.read_csv(be_droped)
data_new = pd.Series(data["Label"])
data_new.to_csv(new_csv,index=0)
data = data.drop(["Label"],axis=1)
data.to_csv(be_droped,index=0)