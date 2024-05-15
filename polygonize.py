import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\User\stella-ai_preprocessing\0021061_027.png'

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

# Example usage
if __name__ == "__main__":
    # Load segmented mask image
    mask_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Polygonize the mask image
    points_list = polygonize_mask(mask_image)

    # Print the extracted points    
    for i, points in enumerate(points_list):
        print(f"Contour {i+1} points: {points}")

    # plot the points_list using matplotlib
    for points in points_list:
        x, y = zip(*points)
        plt.plot(x, y)

    plt.gca().invert_yaxis()  # Invert y-axis to match image coordinate system
    plt.show()