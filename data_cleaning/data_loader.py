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


def load_compressed_pic(file_path, file_name):
    # load numpy array from npz file
    # load dict of arrays
    data = np.load(f"{file_path}/{file_name}")
    return data


def select_files_from_balanced_label(select_label_per_class, train_labels_df):
    # Note that we have almost balanced labels from the training dataset, around 450 each.
    select_files = []
    for i in range(250):
        select_files += (list(train_labels_df[train_labels_df['label'] == 5]['img_name'].values[:select_label_per_class]))
    return select_files


def main(pics_folder_path, output_path):
    input_file_list = os.listdir(pics_folder_path)
    total_files_number = len(input_file_list)
    for i in range(total_files_number):
        data_loading_transform_save(pics_folder_path, input_file_list[i], output_path)
        print(f"{((i + 1) / total_files_number)*100} % complete")

    print("**")
    print("ALL PICS ARE CONVERTED")
    print("**")

