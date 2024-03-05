import matplotlib.pyplot as plt
import cv2
import os
import numpy as np

mask_dir = './mask'
plotted_mask_dir = './plotted_mask'

for folder in os.listdir(mask_dir):
    for image in os.listdir(os.path.join(mask_dir, folder)):

        img = cv2.imread(os.path.join(mask_dir, folder, image))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  

        blank = np.zeros_like(img)
        cv2.drawContours(blank, contours, -1, (0, 0, 255), -1) 
        
        img_uint8 = np.uint8(img)
        blank_uint8 = np.uint8(blank)

        result = cv2.add(img_uint8, blank_uint8)
        print(result)

        plt.imsave(os.path.join(plotted_mask_dir, folder + '_' + image.split('.')[0] + '.png'), cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    