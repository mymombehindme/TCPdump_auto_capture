執行環境:windows 10 python 3.8.5

執行前先確認
修改python檔中dataset路徑確認是否正確，dataset.csv包含了良性和惡意flow，用於訓練模型，dataset_test.csv用於測試單一flow，dataset.csv不包含dataset_test.csv內流量

安裝套件:
$pip install pandas
$pip install xgboost
$pip install lightgbm
$pip install catboost
$pip install scikit-learn
$pip install matplotlib
$apt-get install python-tk
$pip install seaborn

執行的方式為
$./easy.sh [要轉換的pcap]//要轉換的pcap請輸入字串

//請在github下載一個開源軟件，名稱為TCPDUMP_and_CICFlowMeter，會用到裡面的一個執行檔，名稱為convert_pcap_csv.sh

//github網址:https://github.com/iPAS/TCPDUMP_and_CICFlowMeter

$python auto_label.py [要label的csv] [種類]//要label的csv請輸入字串，種類請輸入數字

//例子  python auto_label.py Geodo.pcap_Flow.csv 3  其結果將會輸出Geodo.pcap_Flow_with_label.csv

$python total.py [要被讀取的csv] [所有種類集合的csv] [從要被讀取的csv中取出的數量]//前二者輸入字串，後者輸入數字

//分類惡意流量前，先將所有不同惡意種類的流量封包存成一個csv，要有多少封包可以自行決定數量

$python drop.py [所有種類集合的csv]//型態為字串

//集中成一個csv_file後，使用drop.py後，會多出一個attack_type檔案，此檔案將label欄位單獨存放，而這兩個csv為後來要輸入classifier的引數

$python xgb_classifier.py [所有種類集合的csv] [所有種類集合的attact_type]//都為字串

//執行xgb分類，程式中使用train_test_split會將所有資料自行分類為測試集與訓練集各1/2，並且將產出的模型存入test_model

$python cat.py [所有種類集合的csv] [所有種類集合的attact_type]//都為字串

//執行cat分類，程式中使用train_test_split會將所有資料自行分類為測試集與訓練集各1/2，並且將產出的模型存入test_model

$python lightBGM.py [所有種類集合的csv] [所有種類集合的attact_type]//都為字串

//執行lightBGM分類，程式中使用train_test_split會將所有資料自行分類為測試集與訓練集各1/2，並且將產出的模型存入test_model
