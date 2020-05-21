import os
import math
import numpy as np
from scipy import misc
from imageio import imread, imwrite

print('Scale: ')
N = input()
try:
    P = float(N)
except ValueError:
    print('ValueError: floating your scale:', N)
    exit (0)
    
print("P =", P)

inputfile=input("Enter name of input file: ")
if not os.path.exists(inputfile):
    print("error: unable to open file")
    exit(0)
im1=imread(inputfile)
h=len(im1)      # высота изображения = длина списка строк изображения
w=len(im1[0])   # ширина изображения = длина списка одной строки
print('width=',w, 'height=',h, 'size=',w*h*4)
outputfile=input("Enter name of output file: ")
im1=im1.astype('uint8')


if(P>=1):

    u = math.floor(P)
    if (u+0.5 > P):
        n = u
    else:
        n = u+1
    print("n =",n)
          
    im2=np.ones((n*h,n*w,3))
    im2=im2.astype('uint8')
    for ix in range (0, w):
        print(ix, '/', w-1);
        for iy in range(0, h):
            for i in range ((ix)*n,(ix+1)*n):
                for j in range ((iy)*n,(iy+1)*n):
                    im2[j][i]=im1[iy][ix]
                    #im2[j][i][1]=im1[iy][ix][1]
                    #im2[j][i][2]=im1[iy][ix][2]
else:
    U = float(1/P)
    print ("U =",U)
    u = math.floor(U)
    if (u+0.5 > U):
        n = u
    else:
        n = u+1
    print("n =",n)
    
    W = math.floor(w/n)
    print("W =", W)
    H = math.floor(h/n)
    print("H =", H)
    
    im2=np.ones((H,W,3))
    im2=im2.astype('uint8')
    for ix in range (0, W):
        print(ix, '/', W-1)
        for iy in range(0, H):            
            for i in range ((ix)*n,(ix+1)*n):
                for j in range ((iy)*n,(iy+1)*n):
                    im2[iy][ix]+=im1[j][i]
                    #im2[iy][ix][1]+=im1[j][i][1]
                    #im2[iy][ix][2]+=im1[j][i][2]
            im2[iy][ix][0] = (im2[iy][ix][0] / n)
            im2[iy][ix][1] = (im2[iy][ix][1] / n)
            im2[iy][ix][2] = (im2[iy][ix][2] / n)
        
imwrite(outputfile,im2,format='bmp')
print("Please, check your", outputfile, "file")
exit(0)
