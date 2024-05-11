import cv2
import os

def change_3_to_1_channel():
    path = 'D:\stella_ai_learning\plotted_mask'
    for filename in os.listdir(path):
        img = cv2.imread(os.path.join(path, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(path, filename), gray)
        
change_3_to_1_channel()