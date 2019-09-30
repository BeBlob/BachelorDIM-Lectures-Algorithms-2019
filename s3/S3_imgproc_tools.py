"""
@author: BeBlob
"""

import cv2
import numpy as np 

"""Documentation for invert_colors_manual
@return ndarray
    a matrix representing the image inverted
@param input_img
    an image
Invert an image manually
"""
def invert_colors_manual(input_img):

    img = cv2.imread(input_img) 
    cv2.imshow("inverted input", input_img)
    cv2.waitKey()

    #display the matrix shapes
    print("image shape = "+str(img.shape))

    #invert the img
    for cmpt_row in range(img.reshape[0]):
        for cmpt_col in range(img.reshape[1]):
            for cmpt_depth in range(img.reshape[2]):
                img[cmpt_row, cmpt_col, cmpt_depth] = 255 - img[cmpt_row, cmpt_col, cmpt_depth]

    #display the loaded images
    cv2.imshow("inverted input", img)
    cv2.waitKey()

    return img






