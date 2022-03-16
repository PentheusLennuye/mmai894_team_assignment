import cv2
import numpy as np
import os


def data_loading_transform_save(file_path, file_name, output_path):
    # Load color imagde
    bgr_img = cv2.imread(f"{file_path}/{file_name}")
    # Convert to grayscale
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    # Normalize, rescale entries to lie in [0,1]
    gray_img = gray_img.astype("float32")/255
    file_output_name = file_name.split(".")[0]
    np.savez_compressed(f'{output_path}/{file_output_name}.npz', gray_img)
    del gray_img
    print(f'{file_name} converted')


def load_compressed_pic(file_path, file_name):
    # load numpy array from npz file
    # load dict of arrays
    data = np.load(f"{file_path}/{file_name}")
    return data


def main(pics_folder_path, output_path):
    input_file_list = os.listdir(pics_folder_path)
    total_files_number = len(input_file_list)
    for i in range(total_files_number):
        data_loading_transform_save(pics_folder_path, input_file_list[i], output_path)
        print(f"{((i + 1) / total_files_number)*100} % complete")

    print("**")
    print("ALL PICS ARE CONVERTED")
    print("**")

