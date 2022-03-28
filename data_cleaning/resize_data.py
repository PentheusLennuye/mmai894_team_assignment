import cv2


def resize_image_set(data, target_length, target_width):
    resized_data = []
    for i in data:
        resresized_imgized = cv2.resize(i, (target_length, target_width), interpolation=cv2.INTER_AREA)
        resized_data.append(resresized_imgized)
    return resized_data
