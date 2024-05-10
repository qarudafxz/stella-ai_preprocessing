import matplotlib.pyplot as plt
import cv2

def extract_mask(file_path):
    """
    Read an image, convert value of mask to 1 for ischemic
    and display the mask.
    
    Parameters:
        file_path (str): The path to the image file.
    """
    try:
        img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError("Could not read the image file.")
    except Exception as e:
        print(f"Error: {e}")
        return
    
    img[img == 255] = 0

    print(img[0][0])
    
    plt.imshow(img, cmap='gray')
    plt.title('Ischemic Stroke Mask')
    plt.axis('off')
    plt.show()

def main():
    file_path = './plotted_mask/0021061_019.png'
    extract_mask(file_path)

if __name__ == "__main__":
    main()
