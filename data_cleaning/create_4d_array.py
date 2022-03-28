#!/usr/bin/env python3
'''
Pull a number of jpeg files for each label, then save a 4d numpy array to file
along with a label file.

usage: create_4d_array.py [-h] [-v] [-i INCLUDE] [-x WIDTH] [-y HEIGHT] [-n NUMBER] -o OUTPUT <split>

   where <split> is test, train, or val;
   INCLUDE is a comma-delimited list of labels, e.g. 211,232,342;
   NUMBER is the number of images per label; and
   OUTPUT is a path and file prefix

example:
   export WORKDIR=MMAI2022_Watts/images
   data_cleaning/create_4d_array.py -v -i 211,243,252 -x 128 -y 128 -n 10 \
        -o data_cleaning/training_samples train

   Creates a (30, 128, 128, 3) numpy array from MMAI2022_Watts/images/train_info.csv
   and the images in MMAI2022_Watts/images/train_set
   and saves it to data_cleaning/training_samples_X.npy, along with matching
   labels in data_cleaning/training_samples_Y.npy

   If INCLUDE is not set, all labels are included.
'''

import argparse
import csv
import os
import random

import cv2
import numpy as np
import tqdm

WORKDIR = os.getenv('WORKDIR',
                    os.path.join('MMAI2022_Watts', 'images'))

DEFAULT_NUM_IMAGES = 5
DEFAULT_WIDTH = 256
DEFAULT_HEIGHT = 256

ERR_FAILED_IMAGE = 1

class FourDFromFiles:
    '''
    Takes a directory full of images by consulting the "info" csv file, then
    converts them into a uniform 4d numpy array, and saves them.'''

    def __init__(self):
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.num_images = DEFAULT_NUM_IMAGES
        self.split = None
        self.output_filepath = None
        self.verbose = False
        self.file_list = {}  # keyed to label
        self.images = []  # The 3d numpy array
        self.labels = []  # A vector of labels
        self.include = []

        self.__process_arguments()
        if self.verbose:
            print(f"Processing first {self.num_images} files for split "
                  f"{self.split}: setting to ({self.width}x{self.height})")
        self.__set_img_array()
        if self.verbose:
            print('Stacking to 4d')
        img_4d_array = np.stack(self.images, axis=0)  # This is our 4d array
        self.__write_files(img_4d_array)
        print('Shape of saved array: ', img_4d_array.shape)

    def __process_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--verbose', action='store_true')
        parser.add_argument('-i', '--include', default=DEFAULT_WIDTH, type=str,
                            help='Comma-delimited list of included labels')
        parser.add_argument('-x', '--width', default=DEFAULT_WIDTH, type=int,
                            help='Output width of the numpy image')
        parser.add_argument('-y', '--height', default=DEFAULT_HEIGHT, type=int,
                            help='Output height of the numpy image')
        parser.add_argument('-n', '--number', default=DEFAULT_NUM_IMAGES, type=int,
                            help='The number of images to load')
        parser.add_argument('-o', '--output', type=str, required=True,
                            help='The output numpy file')
        parser.add_argument('split',
                            help='train, test, or val')
        args = parser.parse_args()
        self.include = args.include.split(',')
        self.num_images = args.number
        self.width = args.width
        self.height = args.height
        self.split = args.split
        self.verbose = args.verbose
        self.output_filepath = args.output

    def __set_img_array(self):
        csv_file_path = os.path.join(WORKDIR, self.split + '_info.csv')
        image_file_dir = os.path.join(WORKDIR, self.split + '_set')
        with open(csv_file_path, encoding='utf8') as csvfile:
            csv_reader = csv.reader(csvfile)
            return self.__set_array_from_csv(csv_reader, image_file_dir)

    def __set_array_from_csv(self, csv_reader, image_file_dir):
        # Ensure that every label is represented
        self.__build_file_list(csv_reader)
        self.__add_images_from_file_list(image_file_dir)

    def __build_file_list(self, csv_reader):
        for row in csv_reader:
            if self.include and row[1] not in self.include:
                continue
            if row[1] not in self.file_list:
                self.file_list[row[1]] = []
            self.file_list[row[1]].append(row[0])
        if self.verbose:
            num_labels = len(self.file_list)
            print(f"Number of labels: {num_labels}")

    def __add_images_from_file_list(self, image_file_dir):
        for item in tqdm.tqdm(self.file_list.items()):
            label = item[0]
            filename = item[1]
            samples = random.sample(
                filename, self.num_images
            )
            for filename in samples:
                image_file_path = os.path.join(image_file_dir, filename)
                if self.__add_image_from_file(image_file_path):
                    self.labels.append(label)

    def __add_image_from_file(self, image_file_path):
        try:
            im_bgr = cv2.imread(image_file_path) # bgr is like rgb
            if im_bgr is None:
                print(f"Unable to load {image_file_path}")
            im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)  # Not needed ?
            img_rgb_resized = cv2.resize(
                im_rgb,
                (self.width, self.height),
                interpolation=cv2.INTER_CUBIC
            )
        except ValueError:
            print(f"ValueError Exception loading {image_file_path}")
            return False
        self.images.append(img_rgb_resized)
        return True

    def __write_files(self, img_array):
        if self.verbose:
            print("Saving numpy as pickle")
        np.save(self.output_filepath + '_X.npy', img_array, allow_pickle=True)
        if self.verbose:
            print("Saving labels as npy")
        np.save(self.output_filepath + '_Y.npy',
                np.asarray(self.labels),
                allow_pickle=True
        )

if __name__ == '__main__':
    FourDFromFiles()
