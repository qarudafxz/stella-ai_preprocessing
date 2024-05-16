import os
import cv2

root_dir = r'C:\Users\User\Downloads\hemorrhagic_ct-20240515T122518Z-001\hemorrhagic_ct'
brain_dir = r'C:\Users\User\stella-ai_preprocessing\hemorrhagic_datasets\mask'

for folder in os.listdir(root_dir):
    # enter each folder
    for folders in os.listdir(os.path.join(root_dir, folder)):
        if folders == 'mask':
            #save the images in brain_dir with the following name format of the file (root_folder_name + image_name)
            for image in os.listdir(os.path.join(root_dir, folder, folders)):
                img_path = os.path.join(root_dir, folder, folders, image)
                try:
                    img = cv2.imread(img_path)
                    if img is None:
                        print(f"Failed to read image: {img_path}")
                    else:
                        img_png = os.path.splitext(image)[0] + '.png'
                        # rename first the image by removing the '_HGE_SEG' in the image name
                        img_png = img_png.replace('_HGE_Seg', '')
                        cv2.imwrite(os.path.join(brain_dir, folder + '_' + img_png), img)
                        print(f"Image saved: {os.path.join(brain_dir, folder + '_' + img_png)}")
                except Exception as e:
                    print(f"Error processing image '{img_path}': {e}")
