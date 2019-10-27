import os 
import glob
import re
import pandas as pd
#file_pwd=os.path.basename('C:\\jimmy\\fbauto\\pythontest\\output\\*')
def etot_selection(folderpwd):
    folderpwd=folderpwd+'*'
    etot=[]
    for filename in glob.glob(folderpwd):
        #輸入你Output的資料夾位置 *代表所有檔案
        temp_file=[]
        fopen=open(filename)
        for line in fopen:
            temp_file.append(line)
        fopen.close()
        #開啟檔案逐行複製至站存的list
        p_head=temp_file.index("      A V E R A G E S   O V E R     100 S T E P S\n")#定位能量位置
        del temp_file[0:p_head+4]
        del temp_file[1:-1]
        temp_file=str(temp_file)
        temp_file=re.split('\s+',temp_file)
        #取出etot後能量
        etot.append(temp_file[3])
    return etot
#etot_energy_list=etot_selection('C:\\jimmy\\fbauto\\pythontest\\output\\')
etot_energy_list=etot_selection(input("請輸入你的input資料夾"))
energy=pd.DataFrame(etot_energy_list)
#finalcsv=pd.read_excel('C:\\jimmy\\fbauto\pythontest\\DHB_MD+GIST.xlsx',sheet_name='Structure Relaxation Ⅱ',encoding='big5')
#格式問題，請存成CSV再次開啟
#finalcsv=pd.read_csv('C:\\jimmy\\fbauto\\pythontest\\DHB_MD+GIST.csv')
finalcsv=pd.read_csv(input("讀取excel檔案名稱(包括路徑)"))
finalcsv.columns=range(finalcsv.shape[1])
##從3,12開始
##csv從3,11開始
for i in range(len(energy)):
    finalcsv.iloc[3,11+i]=energy.iloc[i,0]
#finalcsv.to_csv('C:\\jimmy\\fbauto\\pythontest\\DHB_MD+GISTfinal.csv',encoding='big5',header=None,index=False)
finalcsv.to_csv(input("你的輸出excel檔案名稱(包括路徑)"),encoding='big5',header=None,index=False)