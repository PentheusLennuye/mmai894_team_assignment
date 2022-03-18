#!/usr/bin/env python3
'''
Spike: a demonstration of how to get a 4d numpy array from a bunch of
jpegs. This is just for 5 images on train info.
'''

import csv
import numpy as np
import os
import sys

import cv2

NUM_IMAGES = 5
WIDTH = 256
HEIGHT = 256

ERR_FAILED_IMAGE = 1
WORKPATH = 'MMAI2022_Watts'

images = []
with open(os.path.join(WORKPATH, 'images', 'train_info.csv')) as csvfile:
    train_info = csv.reader(csvfile)
    i = 0
    for row in train_info:
        i += 1
        if i > NUM_IMAGES:
            break
        filepath = os.path.join(WORKPATH, 'images', 'train_set', row[0])
        print(filepath)  # Just so we know where we're at
        try:
            im_bgr = cv2.imread(filepath) # bgr is like rgb, but different
            if im_bgr is None:
                print(f"Unable to load {filepath}")
        except Exception:
            print(f"Exception loading {filepath}")
            continue

        im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)  # Not needed ?
        im_rgb_resize = cv2.resize(im_rgb,
                                   (WIDTH, HEIGHT),
                                   interpolation=cv2.INTER_CUBIC)
        images.append(im_rgb_resize)
        
my_array = np.stack(images, axis=0)  # This is our 4d array
np.save(WORKPATH, 'spike_4d.npy', allow_pickle=True)

