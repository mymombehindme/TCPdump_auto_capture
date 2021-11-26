#!/bin/bash
file_name=$1
copy_file_name=${file_name:0:-5}"_backup.pcap"


cp $file_name $copy_file_name
#echo "copy file...."


~/new_CIC/TCPDUMP_and_CICFlowMeter/convert_pcap_csv.sh $1
