import numpy as np


def resample_data(data, label, selected_label_list):
    select_labels = []
    select_data = []
    for i in range(len(label)):
        current_label = label[i]
        if current_label in selected_label_list:
            select_labels.append(current_label)
            select_data.append(data[i])
    select_labels = np.asarray(select_labels)
    select_data = np.asarray(select_data)

    return select_data, select_labels


def mapping_new_label(select_label_from_original):
    s_l_dict = {}
    for i in range(len(select_label_from_original)):
        s_l_dict[select_label_from_original[i]] = i
    return s_l_dict