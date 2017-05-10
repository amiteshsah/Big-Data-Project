# Big-Data-Project
Cleaning and Analysis of NYC crime data and further investigate relationship with other dataset(s).

Archive Contents:

Analysis: Implemented with Hadoop map reduce using python for the analysis of NYC Crime data.
  1)Attempted_vs_Boroughs_map.py and Attempted_vs_Boroughs_reduce.py
  2)CrimeDesc_vs_Boroughs_map.py and CrimeDesc_vs_Boroughs_reduce.py
  3)CrimeTypes_vs_Boroughs_map.py and CrimeTypes_vs_Boroughs_reduce.py
  4)DangerousDrugs_vs_Boroughs_map.py and DangerousDrugs_vs_Boroughs_reduce.py
  5)FMVcount_vs_Day_map.py and FMVcount_vs_Day_reduce.py
  6)FMVcount_vs_Time_map.py and FMVcount_vs_Time_reduce.py
  7)FMVcount_vs_Year_map.py and FMVcount_vs_Year_reduce.py
  8)MajorCrimeRate_vs_Boroughs_map.py and MajorCrimeRate_vs_Boroughs_reduce.py

ColumnValidators : It contains map code for all the columns to check if the value is valid, invalid or null. 
There is a common reduce function to create single cleaned file
File Details:

  1)CMPLNT_NUM_Validator_map.py
  2)CMPLNT_FR_DT_Validator_map.py
  3)CMPLNT_FR_TM_Validator_map.py
  4)CMPLNT_TO_DT_Validator_map.py
  5)CMPLNT_TO_TM_Validator_map.py
  6)RPT_DT_Validator_map.py
  7)KY_CD_Validator_map.py
  8)OFNS_DESC_Validator_map.py
  9)PD_CD_Validator_map.py
  10)PD_DESC_Validator_map.py
  11)CRM_ATPT_CPTD_CD_Validator_map.py
  12)LAW_CAT_CD_Validator_map.py
  13)JURIS_DESC_Validator_map.py
  14)BORO_NM_Validator_map.py
  15)ADDR_PCT_CD_Validator_map.py
  16)LOC_OF_OCCUR_DESC_map.py
  17)PREM_TYP_DESC_Validator_map.py
  18)PARKS_NM_Validator_map.py
  19)HADEVELOPT_Validator_map.py
  20)X_COORD_CD_Validator_map.py
  21)Y_COORD_CD_Validator_map.py
  22)Latitude_Validator_map.py
  23)Longitude_Validator_map.py
  24)Lat_Lon_Validator_map.py


convert_txt_to_csv.py : it converts the text file from hadoop output to csv file.
map_time.py : It is map function for the data cleaning
total_Reduce.py : It is the reduce function for cleaning the full input file. It contains function for each column and checks, validates                   and modifies the data if necessary so that we can have better output file that can be convinent for analysis .

Setup: 

Step 1: Check the version of python and shapely and create a python wrapper script
Python 2.7.11 version
Shapely 1.5.13 version

Install shapely by informing the HPC Administrator

1/ Create a python wrapper script:
$ cat python-2.7.11_wrp.sh
#!/bin/bash
source /etc/profile.d/modules.sh
module purge
module load python/gnu/2.7.11
python $*

2/ Submit your hadoop jobs like (please adjust parameters accordingly):
$ hadoop jar /opt/cloudera/parcels/CDH-5.4.5-1.cdh5.4.5.p0.7/jars/hadoop-streaming-2.6.0-cdh5.4.5.jar -D mapred.reduce.tasks=1 -files "python-2.7.11_wrp.sh,mapper.py,reducer.py"   -mapper "python-2.7.11_wrp.sh mapper.py" -reducer "python-2.7.11_wrp.sh reducer.py" -input /user/aks629/in/005 -output /user/aks629/out/032


step 2: Steps needed to run the code :
  2a) For validating each columns :
    In local machine: Change the Directory to the ColumnValidators Folder
      cat $/File/path | python $column_map.py | sort -n | python $cleanReduce.py
    In Hadoop :
    For all the column except latitude and longitude columnn
      hjs -D mapred.reduce.tasks=1 -files "<column_map.py>,cleanReduce.py"   -mapper "<column_map.py>" -reducer "cleanReduce.py" -input /user/aks629/NYPD_Complaint_Data_Historic.csv -output /user/aks629/out
 
    For Latitude and Longitude cloumn ,
      hjs -D mapred.reduce.tasks=1 -files "python-2.7.11_wrp.sh,Lat_Lon.py,cleanReduce.py,query.txt"   -mapper "python-2.7.11_wrp.sh Lat_Lon.py" -reducer "python-2.7.11_wrp.sh cleanReduce.py" -input /user/aks629/NYPD_Complaint_Data_Historic.csv -output /user/aks629/C23
 
  2b) For cleaning the data
    In local machine:
    cat $/File/path | python map_time.py | python total_Reduce.py
    In Hadoop:
     hjs -D mapred.reduce.tasks=10 -files "python-2.7.11_wrp.sh,map_time.py,totalReduce.py,query.txt"   -mapper "python-2.7.11_wrp.sh map_time.py" -reducer "python-2.7.11_wrp.sh totalReduce.py" -input /user/aks629/NYPD_Complaint_Data_Historic.csv -output /user/aks629/final_output
     
     2c) For analyzing the data
     In local machine
     cat filename | python file_map.py | sort -n | python file_reduce.py
     In Hadoop machine:
      hjs -files /home/aks629/Big_Data_Project/Analysis/file_map.py,/home/aks629/Big_Data_Project/Analysis/file_reduce.py -mapper "file_map.py" -reducer "file_reduce.py" -numReduceTasks 1 -input /user/aks629/final_output.csv -output C_out
     
    
    Part 2:
    We used Map Reduce to clean NYC 311 Complaint data that had 52 columns. So this is the map reduce code:
map311.py
reduce311.py
Initially we ran with 10 cluster nodes but it would take lot of time to run. So to reduce the running time , we optimized it by changing the number of reducers to 1000 to clean complaint data. We had to include a wrapper mod.sh  so that we could run shapefile in hadoop. 
This is the command we used to run the code:
hjs -D mapred.reduce.tasks=1000 -files "mod.sh,map311.py,reduce311.py,query.txt"  -mapper "mod.sh map311.py" -reducer "mod.sh reduce311.py" -input /user/aks629/311.csv -output /user/aks629/final_complaint.out

We then used hfs -getmerge to combine those 1000 output part file and get that file locally. This txt file was converted to csv file by using a simple python code  convert_txt_to_csv.py . 

We used map reduce code to perform JOIN ( set ) operation by NTA code . We had two files CombinedProperties_vs_Neighbourhoods.csv and Crimerate.csv. So we had to merge this two file to one by their NTA code , so that it would be easier to plot the data and prove our hypothesis by Neighbourhood. Following are the map reduce code:
CombinedRatesperYear_vs_CrimeRate_map.py
CombinedRatesperYear_vs_CrimeRate_reduce.py

Similar JOIN operation was performed for CombinedProperties_vs_Neighbourhoods.csv and 311_Complaintrate.csv. We used one mapper and one reducer.
f1_f2_map.py
f1_f2_reduce.py


We wrote the Map Reduce code to assemble all the coordinates where crime was committed in crime data to one list by Neighbourhood name. We used one mapper and 4 reducers.
map_NTA_coordinates.py
reduce_NTA_coordinates.py

