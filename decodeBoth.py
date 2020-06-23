# run: python3 decodeBoth.py -pc poly_coefs.npy -number 30
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='number and polycoefs')
parser.add_argument('-number', '--number', type=int, metavar='', help='number of values')
parser.add_argument("-pc", "--pc", required = True, help = "matrix of coefficients");
args = vars(parser.parse_args());

args = parser.parse_args()

def decode(pc, number):
    poly_coefs=np.load(pc)
    #print(poly_coefs.shape)
    if poly_coefs.shape[2]==3: #colors
        matrix=np.zeros((poly_coefs.shape[0],poly_coefs.shape[1], poly_coefs.shape[2], number))
        x=np.arange(number)
    
        for i in range(poly_coefs.shape[0]):
            for j in range(poly_coefs.shape[1]):
                for k in range(poly_coefs.shape[2]):
                    coefs=(poly_coefs[i,j,k,:])
#            #print(np.polyval(coefs,x))
                    matrix[i,j,k,:]=np.polyval(coefs,x)
        matrix=np.clip(matrix, 0, 1) #to avoid: lipping input data to the valid range for imshow with RGB data ([0..1] for floats or [0..255] for integers). 
        if np.any(np.isnan(matrix)) == False:
            print("no NaN found")
        else:
            print("NaN found, some pixels will be lost")
        if np.any(np.isinf(matrix)) == False:
            print("no inf found")
        else:
            print("inf found, some pixels will be lost")

          
        np.save("matrix.npy",matrix)
        for nr in range(number):
            plt.imshow(matrix[:,:,:,nr])
            plt.show()
   
    else:
        matrix=np.zeros((poly_coefs.shape[0],poly_coefs.shape[1],number))
        x=np.arange(number)
    
        for i in range(poly_coefs.shape[0]):
            for j in range(poly_coefs.shape[1]):
                coefs=(poly_coefs[i,j,:])
            #print(np.polyval(coefs,x))
                matrix[i,j,:]=np.polyval(coefs,x)
    
        if np.any(np.isnan(matrix)) == False:
            print("no NaN found")
        else:
            print("NaN found, some pixels will be lost")
        if np.any(np.isinf(matrix)) == False:
            print("no inf found")
        else:
            print("inf found, some pixels will be lost")    


        np.save("matrix.npy",matrix)
        for nr in range(number):
            plt.imshow(matrix[:,:,nr], cmap='gray')
            plt.show()
if __name__ == "__main__":
    decode(args.pc,args.number)
