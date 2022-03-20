#!/usr/bin/env python3
'''
Create and save a 4d numpy array to file.

usage: create_4d_array.py [-h] [-v] [-x WIDTH] [-y HEIGHT] [-n NUMBER] -o OUTPUT <split>

where <split> is test, train, or val
'''

import argparse
import csv
import os
import random

import cv2
import numpy as np
import tqdm

WORKDIR = os.path.join('..', 'MMAI2022_Watts', 'images')

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

        self.__process_arguments()
        if self.verbose:
            print(f"Processing first {self.num_images} files for split "
                  f"{self.split}: setting to ({self.width}x{self.height})")
        self.__set_img_array()
        img_4d_array = np.stack(self.images, axis=0)  # This is our 4d array
        if self.verbose:
            print(f"Writing {self.output_filepath}")
        self.__write_file(img_4d_array)
        print('Shape of saved array: ', img_4d_array.shape)

    def __process_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--verbose', action='store_true')
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
            if row[1] not in self.file_list:
                self.file_list[row[1]] = []
            self.file_list[row[1]].append(row[0])
        if self.verbose:
            print("Number of labels: %s", len(self.file_list))

    def __add_images_from_list_list(self, image_file_dir):
        for item in tqdm.tqdm(self.file_list.items()):
            label_samples = random.sample(
                item[1], self.num_images
            )
            for filename in label_samples:
                image_file_path = os.path.join(image_file_dir, filename)
                self.__add_image_from_file(image_file_path)

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

    def __write_file(self, img_array):
        np.save(
            os.path.join(self.output_filepath), img_array, allow_pickle=True
        )


if __name__ == '__main__':
    FourDFromFiles()
