import os
import numpy as np
import pandas as pd
import re
import glob
#os.chdir('D:\\temdpp\\dattest\\')
def structure_selection(folderpwd):
        folderpwd=folderpwd+'*'
        selection=[]
        temp_filelist=glob.glob(folderpwd)
        empty_df=pd.DataFrame()
        for filename in temp_filelist:
                print(filename)
                fileopen=np.loadtxt(filename) 
                filename=pd.DataFrame(fileopen)
                selection.append(filename)
                data_datDF.to_csv('test.csv',index=False)
                for i in range(48,70):
                        Ang1 =filename[1] <= 85 
                        Ang1_1 = filename[1] >=75
                        Ang2 = filename[2] <= 93 
                        Ang2_1 =84 <= filename[2]
                        Ang3 = filename[3] <= 90 
                        Ang3_1 = 82 <= filename[3]
                        Ang4 = filename[4] <= 92 
                        Ang4_1 = 82 <= filename[4]
                        a=(i+2)*0.1
                        b=(i-2)*0.1
                        dissel = filename[5] <= a
                        dissel2 = b <= filename[5]      
                        Ang = filename[Ang1 & Ang1_1 & Ang2 & Ang2_1 & Ang3 & Ang3_1 & Ang4 & Ang4_1 & dissel & dissel2]
                        column_name=range(1,6)
                        Ang[0]=Ang[0].apply(int)
                        final_df=Ang.set_index(0)
                        final_df=final_df[column_name]
                        print(final_df)
                        final_df=pd.DataFrame(final_df)
                        finalcsv=pd.concat([empty_df,final_df],axis=0)
            #finalcsv.to_csv('final.csv',index=True)
            #finalcsv.to_csv('final.csv',index=True)
        return finalcsv 
finalcsv=structure_selection('D:\\temdpp\\dattest\\dat\\')
finalcsv.to_csv('D:\\temdpp\\dattest\\final.csv',header=0)
#finalcsv.to_csv('final.csv',index=True)
# data_dat = np.loadtxt('5kcal_angle_00048.dat')
# data_datDF = pd.DataFrame(data_dat)
# data_datDF.to_csv('test.csv',index=False)
# Ang1 =data_datDF[1] <= 85 
# Ang1_1 = data_datDF[1] >=75
# Ang2 = data_datDF[2] <= 93 
# Ang2_1 =84 <= data_datDF[2]

# Ang3 = data_datDF[3] <= 90 
# Ang3_1 = 82 <= data_datDF[3]

# Ang4 = data_datDF[4] <= 92 
# Ang4_1 = 82 <= data_datDF[4]

# dissel = data_datDF[5] <=5  
# dissel2 = 4.6 <= data_datDF[5]

# Ang = data_datDF[Ang1 & Ang1_1 & Ang2 & Ang2_1 & Ang3 & Ang3_1 & Ang4 & Ang4_1 & dissel & dissel2]
# column_name=range(1,6)
# Ang[0]=Ang[0].apply(int)
# final_df=Ang.set_index(0)

# final_df=final_df[column_name]
# print(final_df)
# final_df.to_csv('final.csv',index=True)

