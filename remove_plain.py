import os
import cv2
import numpy as np

"""

TODO: Remove plain black images from the dataset based on no pixel values

Remain only images with pixel values in the same file path

"""

mask_path = r"C:\Users\User\Desktop\HACK4HEALTH\HACKATHON_PRO\train\mask"
train_path = r"C:\Users\User\Desktop\HACK4HEALTH\HACKATHON_PRO\train\image"

def remove_black_images():
    for root, dirs, files in os.walk(train_path):
        for file in files:
            file_path = os.path.join(root, file)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            print(file_path)
            if img is None:
                raise FileNotFoundError("Could not read the image file.")
            if np.count_nonzero(img) == 0:
                print("Removing:", file_path)
                os.remove(file_path)

remove_black_images()