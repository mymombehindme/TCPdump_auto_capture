import os
import threading
import random

hOutput = open('dataset.csv', 'w')
hOutput_test = open('dataset_test.csv', 'w')
lock = threading.Lock()

def preTake_ip(attFilename,newFileName):
    lock.acquire()
    hAllFlows=open(attFilename, 'r',encoding="utf-8")
    hOutput_atk=open(newFileName,'w',encoding="utf-8")
    newFlow = hAllFlows.readline()
    hOutput_atk.write(newFlow)
    while True:
        newFlow = hAllFlows.readline()
        if not newFlow: break
        bMal = newFlow.split(',')[-1]
        if bMal != "1\n" :
            hOutput_atk.write(newFlow)
    hAllFlows.close()
    hOutput_atk.close()
    lock.release()

def preProc_fn_ip(attFilename,newFileName):
    with open(attFilename, 'r',encoding="utf-8") as hAllFlows:
        hAtkFlows=open(newFileName, 'r',encoding="utf-8")
        newFlow = hAllFlows.readline()
        newFlow_atk = hAtkFlows.readline()
        file_cnt=0
        while True:
            newFlow = hAllFlows.readline()
            newFlow_atk = hAtkFlows.readline()
            if (not newFlow or not newFlow_atk): break
            bMal = newFlow.split(',')[-1]
            if bMal != "1\n" :
                continue
            else:   
                lock.acquire()
                #print(bMal)
                features = newFlow.split(',')
                output = []
                output.extend(features[1:-1])
                #output.append(',')
                output.append("0\n")
                #print(output)
                
                output_atk = []
                features_atk=newFlow_atk.split(',')
                output_atk.extend(features_atk[1:-1])
                output_atk.append("1\n")
                if(file_cnt % 20 == 0):
                    hOutput_test.write(','.join(output))
                    hOutput_test.write(','.join(output_atk))
                else:
                    hOutput.write(','.join(output))
                    hOutput.write(','.join(output_atk))
                lock.release()
                file_cnt+=1
        hAtkFlows.close()

def main():
    threads = []
    for root, dirs, files in os.walk('./dataset'):
        for f in files:
            if '_IP.csv' in f:
                #print(f)
                atk_name=f[:-4]
                atk_name+="_atk.csv"
                #print(os.path.join(root,atk_name))
                threads.append(threading.Thread(target=preTake_ip, args=(os.path.join(root, f),os.path.join(root,atk_name)),))
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()

    column = ['f'+str(i) for i in range(1, 78)]
    hOutput.write(','.join(column)+'\n')
    hOutput_test.write(','.join(column)+'\n')
    with open('./dataset/benign1.pcap.csv', 'r',encoding="utf-8") as hAllFlows:
        newFlow = hAllFlows.readline()
        for root, dirs, files in os.walk('./dataset'):
            for f in files:
                if '_label.csv' in f:
                    hAtkFlows=open(os.path.join(root, f), 'r',encoding="utf-8")
                    newFlow_atk = hAtkFlows.readline()
                    if (not newFlow): break
                    file_cnt=0
                    while True:
                        newFlow = hAllFlows.readline()
                        newFlow_atk = hAtkFlows.readline()
                        if (not newFlow or not newFlow_atk or file_cnt>12600): break

                        features = newFlow.split(',')
                        output = []
                        output.extend(features[1:-1])
                        #output.append(',')
                        output.append("0\n")
                        #print(output)

                        features_atk=newFlow_atk.split(',')
                        output_atk = []
                        output_atk.extend(features_atk[1:-1])
                        output_atk.append("1\n")

                        if(file_cnt % 20 == 0):
                            hOutput_test.write(','.join(output))
                            hOutput_test.write(','.join(output_atk))
                        else:
                            hOutput.write(','.join(output))
                            hOutput.write(','.join(output_atk))
                        file_cnt+=1
                    hAtkFlows.close()

    threads = []
    for root, dirs, files in os.walk('./dataset'):
            if len(files) < 2 : continue
            for f in files:
                if '_IP.csv' in f:
                    #print(f)
                    atk_name=f[:-4]
                    atk_name+="_atk.csv"
                    threads.append(threading.Thread(target=preProc_fn_ip, args=(os.path.join(root, f),os.path.join(root,atk_name)),))
    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()
    hOutput.close()
    hOutput_test.close()

if __name__ == '__main__':
    main()