import os
import numpy as np
from scipy import misc
from imageio import imread, imwrite

print('Scale:')
N = input()
n = int(N)
print('InputFile:')
inputfile=input()
print('OutputFile:')
outputfile=input()
im1=imread(inputfile)
#im1=imread('31.jpg')
h=len(im1)      # высота изображения = длина списка строк изображения
w=len(im1[0])   # ширина изображения = длина списка одной строки
print('width=',w, 'height=',h, 'size=',w*h*4)
k = w-1
im2=np.ones((n*h,n*w,3))
im1=im1.astype('uint8')
im2=im2.astype('uint8')

for ix in range (0, w):
    print(ix, '/', k);
    for iy in range(0, h):
        for i in range ((ix)*n,(ix+1)*n):
            for j in range ((iy)*n,(iy+1)*n):
                im2[j][i]=im1[iy][ix]
                #im2[j][i][1]=im1[iy][ix][1]
                #im2[j][i][2]=im1[iy][ix][2]
imwrite(outputfile,im2,format='bmp')
