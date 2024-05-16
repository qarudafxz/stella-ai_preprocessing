import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\User\stella-ai_preprocessing\0019983_011.png'

def polygonize_mask(mask_image):
    # Convert the mask image to binary
    ret, binary_mask = cv2.threshold(mask_image, 0, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract points from contours
    points_list = []
    for contour in contours:
        points = contour.squeeze(axis=1).tolist()
        points_list.append(points)

    return points_list

if __name__ == "__main__":
    mask_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    points_list = polygonize_mask(mask_image)

    for points in points_list:
        x, y = zip(*points)
        plt.plot(x, y, marker='o', markersize=6, linewidth=2, color='r')

    plt.gca().invert_yaxis() 
    plt.show()