import os
import time
import cv2

# IMPORTANT!!
# Use path in path/path/path format not path\path\path format
input_folder_dir = "C:/Users/jack/Pictures/Pasierbiec_2023"
destination_folder_dir = "C:/Users/jack/Pictures/Photos_by_date"

for image in os.listdir(input_folder_dir):
    img_path = input_folder_dir + "/" + image
    date_created = time.localtime(os.path.getctime(img_path))
    if os.path.exists(destination_folder_dir + "/" + date_created.tm_year):
        cv2.imwrite(image, img_path)
