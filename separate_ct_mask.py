"""
 TODO: convert NII files to JPG
 then set the channels of JPG to 1 instead of 3
 then save the JPG to its corresponding folder
"""

import os
import cv2
import nibabel
import numpy as np
import shutil

path = "D:\stella_ai_learning\Patients_CT"

masks_folder = "D:\stella_ai_learning\hemorrhage_cts\mask"
ct_folder = "D:\stella_ai_learning\hemorrhage_cts\scans"
path = "D:\stella_ai_learning\Patients_CT"


def separate_masks_and_ct():
    for root, dirs, files in os.walk(path):
        for folder in dirs:
            brain_folder = os.path.join(root, folder, "brain")
            if os.path.exists(brain_folder):
                for file in os.listdir(brain_folder):
                    file_path = os.path.join(brain_folder, file)
                    if "HGE_Seg" in file:
                        print("Mask File:", file_path)
                        patient_folder = os.path.basename(root)
                        patient_mask_folder = os.path.join(masks_folder, patient_folder)
                        os.makedirs(patient_mask_folder, exist_ok=True)
                        shutil.copy(file_path, os.path.join(patient_mask_folder, file))
                    else:
                        print("CT Scan File:", file_path)
                        patient_folder = os.path.basename(root)
                        patient_ct_folder = os.path.join(ct_folder, patient_folder)
                        os.makedirs(patient_ct_folder, exist_ok=True)
        
separate_masks_and_ct()