import argparse
import numpy as np
#run: python3 encode.py -k 3
from glob import glob
from skimage.io import imread, imsave
from skimage.color import rgba2rgb, rgb2gray
import math
import argparse
parser = argparse.ArgumentParser(description='number of values')
parser.add_argument('-k', '--k', type=int, metavar='', help='number of values')
args = parser.parse_args()

def encode(k):
    All=[]
    files = glob("*.png") #find all files.png
    for afile in files:
        im = imread(afile) #reading single file = im
       # M=np.array(im) # imread operates on np.array
        #im.show()
        #print(im.shape)
        if im.shape[2]==4:
            rgb=rgba2rgb(im) #4d into 3d
        else:
            rgb=im       
       
        All.append(rgb)    #list of all  images
    many=np.stack((All), axis=-1)   #joining them into one,axis=-1 in this case is the same as axis=3 - size, how many
    #print(many.shape)
    
    numberofpic=len(All) 
    polynom_deg = k
    #poly_coefs=[]
    poly_coefs=np.zeros((many.shape[0],many.shape[1],many.shape[2],polynom_deg+1))
    #print(many.shape)
    #print(poly_coefs.shape)
    x=np.arange(numberofpic) #e.g 4 3x3 matrices joined together, it takes left 'top', this top is 4 long

    for i in range(many.shape[0]): #e.g 100
        for j in range(many.shape[1]):#e.g 189
            for k in range(many.shape[2]):# = 3
                y = many[i,j,k,:] 
            #print('y',y)
            #poly_coefs.append(np.polyfit(x, y, polynom_deg))
                poly_coefs[i,j,k,:]=np.polyfit(x, y, polynom_deg)
    if np.any(np.isnan(poly_coefs)) == False:
        print("no NaN found")
    else:
        print("NaN found, some pixels will be lost")
    if np.any(np.isinf(poly_coefs)) == False:
        print("no inf found")
    else:
        print("inf found, some pixels will be lost")       
   
    np.save("poly_coefs.npy",poly_coefs)
    np.save("many.npy",many)

    
#encode(35)
if (__name__ == "__main__"):
      encode(args.k)
