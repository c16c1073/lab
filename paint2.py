import tensorflow as tf
import keras
from keras.keras.datasets import mnist 
from keras.keras.models import Sequential
from keras.keras.layers import Dense, Dropout, Flatten
from keras.keras.layers import Conv2D, MaxPooling2D
from keras.keras import backend as K
import numpy as np
from PIL import Image

#-----------------------------------------------------必要な情報をロード
pre_naka2=np.load('pre_narutokakasi2.npy')
center_list=np.load('center_list.npy')
img=Image.open('5s/coloring/narutokakasi2.jpg')

print(pre_naka2.shape)
print(center_list.shape)
img.show()


np_img=np.array(img)
#print(np_img)

#----------------------**************予測値を処理*****************---------------------------
print(pre_naka2[0])

list_64=np.argmax(pre_naka2,axis=1)# --行方向の最大値のインデックスをかえす
print(list_64)
print(list_64.shape)


#------------------------------------------------------------------二進数化
import re
'''
#x=list_64[1]
x=49
print(x)
a=''
while(x>0):
        a=str(x%2)+a
        x=int(x/2)
print("なん文字が確認",a)#文字列で二進数化
#print(a.type)

print(len(a))
if len(a)!=6:# 足りない’0’を追加
        b=6-len(a)
        for i in range(b):
                a='0'+a
print(a)

import re# このモジュールは、Perl などと同様の正規表現マッチング操作を提供しています。
#buf='abcdef'
#list = re.split('(..)',buf)[1::2]
#print(list)

a=re.split( '(..)',a )[1::2]#2文字づつに分割
print(a)

n=0
for i in a:# 数値化
    i=int(i)
    a[n]=i
    n+=1

a=np.array(a)
print(a)
'''
#--------------------------------------------


binar_list=[]
for i in list_64:
        #print(i)
        a=''
        while(i>0):
                a=str(i%2)+a
                i=int(i/2)

        if len(a)<6:
                b=6-len(a)
                for n in range(b):
                        a='0'+a

        a=re.split( '(..)',a )[1::2]

        n=0
        for i in a:
                i=int(i)
                a[n]=i
                n+=1
        a=np.array(a)
        binar_list.append(a)
binar_list=np.array(binar_list)
print(binar_list)
print(binar_list.shape)
print(binar_list[1])
#print(binar_list[1][0].type)
#---------------------------------------------------------------------------RGB化

A=0
for i in binar_list:# 二進数からよん段階のRGB値へ
        B=0
        for n in i:
                if n==10:
                        binar_list[A][B]=160
                elif n==11:
                        binar_list[A][B]=224
                elif n==0:
                        binar_list[A][B]=32
                elif n==1:
                        binar_list[A][B]=96
                B+=1
        #print(i)
        A+=1
print(binar_list)


#---------------**************いよいよ、RGB値をinputの座標に入れていく**************----------
# binar_list:RGB値
# center_list:crop毎の真ん中の位置
# あとは、imgとnp_img

print(center_list[0])
print(center_list[1])
print(center_list[2])
print(center_list[3][0])
print(binar_list[0])
print(np_img[0][0])
h,w,d=np_img.shape
print('w,h=',w,h)
#img.show()

A,B=0,0
win_size=42
for i in range(h-win_size):
        for n in range(w-win_size):
                a=int(center_list[A][0])
                b=int(center_list[A][1])
                #print(a,b)
                np_img[b][a]=binar_list[A]
                A+=1
print(np_img)

pil_img=Image.fromarray(np_img)
pil_img.show()












