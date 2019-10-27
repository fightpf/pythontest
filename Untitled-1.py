#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\AI\kaggle_0424'))
	print(os.getcwd())
except:
	pass

#%%
##從mapping.txt取得dictionary
import re
fopen=open("/home/jovyan/CNN/mapping.txt")
text=[]
key=[]
dic=[]
for i in fopen:
    text.append(i)
for i in range(len(text)):
    text[i]=re.split("[\s+,]",text[i])
    key.append(text[i][0])
    dic.append(text[i][2])

dict_labels=dict(zip(key,dic))
print(dict_labels)


#%%
#ref.https://medium.com/%E7%94%A8%E5%8A%9B%E5%8E%BB%E6%84%9B%E4%B8%80%E5%80%8B%E4%BA%BA%E7%9A%84%E8%A9%B1-%E5%BF%83%E4%B9%9F%E6%9C%83%E7%97%9B%E7%9A%84/%E9%BB%98%E9%BB%98%E5%9C%B0%E5%AD%B8deep-learning-3-e9e90c633722

import os
import glob
import numpy as np
from keras.preprocessing.image import  img_to_array, load_img
from PIL import Image
#
size = (256,256) #由於原始資料影像大小不一，因此制定一個統一值
nbofdata=10000   #從各個資料夾中抓取特定數量的檔案
#%%
for folders in glob.glob("/home/jovyan/CNN/train/*"):
    print(folders)
    images=[]
    labels_hot=[]
    labels=[]
    nbofdata_i=1
    for filename in os.listdir(folders):
        if nbofdata_i <= nbofdata:
                    label = os.path.basename(folders)
                    className = np.asarray(label)
                    img=load_img(os.path.join(folders,filename))
                    img=img.resize(size,Image.BILINEAR)
                    if img is not None:
                        if label is not None:
                            labels.append(className)
                            labels_hot.append(dict_labels[label])
                        x=img_to_array(img)
                        images.append(x)
                    nbofdata_i+=1
    images=np.array(images)    
    labels_hot=np.array(labels_hot)
    print("images.shape={}, labels_hot.shape=={}".format(images.shape, labels_hot.shape))    
    imagesavepath='/home/jovyan/CNN/save/'
    if not os.path.exists(imagesavepath):
        os.makedirs(imagesavepath)
    np.save(imagesavepath+'{}_images.npy'.format(label),images)    
    np.save(imagesavepath+'{}_label.npy'.format(label),labels)    
    np.save(imagesavepath+'{}_labels_hot.npy'.format(label),labels_hot)
    print('{} files has been saved.'.format(label))


#%%
import numpy as np
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPooling2D
from sklearn.model_selection import train_test_split
from keras.utils import np_utils


x=np.load('/home/jovyan/CNN/traindata_images.npy')
y=np.load('/home/jovyan/CNN/traindata_labels_hot.npy')
x=x[:,:,:,0].reshape(x.shape[0],256,256,1).astype('float32')
x=x/255
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2, random_state=0)

y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)




model=Sequential()
model.add(Conv2D(filters=16,
                 kernel_size=(3,3),
                 padding='same',
                 input_shape=(256,256,1),
                 activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=36,
                 kernel_size=(5,5),
                 padding='same',
                 activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=48,
                 kernel_size=(3,3),
                 padding='same',
                 activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(filters=64,
                 kernel_size=(5,5),
                 padding='same',
                 activation='relu'))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(15,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
train_history=model.fit(x=x_train,
                        y=y_train,
                        validation_split=0.2,
                        epochs=100,
                        batch_size=300,
                        verbose=2)

model.save('/home/jovyan/CNN/mymodel.h5')


#%%
import os
import glob
import numpy as np
from keras.preprocessing.image import  img_to_array, load_img
from PIL import Image
#
size = (256,256) #由於原始資料影像大小不一，因此制定一個統一值
nbofdata=2000 #從各個資料夾中抓取特定數量的檔案
#%%
folders=('/home/jovyan/CNN/testset')
images=[]
nbofdata_i=1
filelist=os.listdir(folders)
filelist.sort()
print(filelist)
for filename in filelist:
    if nbofdata_i <= nbofdata:
        img=load_img(os.path.join(folders,filename))
        img=img.resize(size,Image.BILINEAR)
        if img is not None:
            x=img_to_array(img)
            images.append(x)
            nbofdata_i+=1
images=np.array(images)      
imagesavepath='/home/jovyan/CNN/kagglehomework'
if not os.path.exists(imagesavepath):
    os.makedirs(imagesavepath)
np.save(imagesavepath+'testset',images)    


#%%
from keras.models import load_model
from keras.models import Sequential
import keras
import pandas as pd
model=Sequential()
model=load_model("/home/jovyan/CNN/mymodel.h5")
x=np.load("/home/jovyan/CNN/kagglehomeworktestset.npy")
x=x[:,:,:,0].reshape(x.shape[0],256,256,1).astype('float32')
x=x/255

result=model.predict(x, batch_size=None, verbose=0, steps=None)
result2=pd.DataFrame(result.argmax(axis=1), columns=['class'])
result2.to_csv('/home/jovyan/CNN/kagglefinal.csv',index=0)


#%%



