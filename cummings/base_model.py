#!/usr/bin/env python3
'''
Base Model for MMAI894 "Cake Detector"
'''

import os

from socketserver import ThreadingMixIn
import numpy as np
import pandas as pd
import sys

import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, Dropout, Conv2D, MaxPooling2D,
                                     Flatten)

'''
CLEANED_DATA = os.path.join('..', 'data_cleaning')
TRAINING_SAMPLES = os.path.join(CLEANED_DATA, 'training_samples.npy')
RANDOM_SEED = 42

training_data_np = np.load(TRAINING_SAMPLES, allow_pickle=True)
# Convert 0 to 255 RGB to 0..1 float
print(training_data_np[0])
sys.exit(1)


# DEPTHS
RGB = 3  # Depth just for reference, not needed in this exercise.
GREYSCALE = 1

DEPTH = GREYSCALE
BATCH_SIZE = 1000  # 35 iterations for 35000 training instances
FILTERS = [64, 128, 256]
KERNEL_SIZE = [7, 3, 3]
STRIDES = [(1, 1), (1, 1), (1, 1)]
PADDING = 'same'  # 'valid' or 'same'. No 'mirror'
DILATION_RATE = [1, 1, 1]
KERNEL_INITIALIZER = 'glorot_uniform'  # Default
INPUT_SHAPE = (28, 28, DEPTH)  # MNIST images
POOL_SIZE = (2, 2)

def build_model():
    model = keras.Sequential(        
        [
            keras.layers.Conv2D(FILTERS[0], KERNEL_SIZE[0],
                                input_shape=INPUT_SHAPE,
                                activation='relu', strides=STRIDES[0],
                                padding=PADDING, dilation_rate=DILATION_RATE[0],
                                kernel_initializer=KERNEL_INITIALIZER,
                                name='c_layer_one'),
            keras.layers.MaxPooling2D(pool_size=POOL_SIZE, padding=PADDING),
            keras.layers.Conv2D(FILTERS[1], KERNEL_SIZE[1],
                                activation='relu', strides=STRIDES[1],
                                padding=PADDING, dilation_rate=DILATION_RATE[1],
                                kernel_initializer=KERNEL_INITIALIZER,
                                name='c_layer_two'),
            keras.layers.Conv2D(FILTERS[1], KERNEL_SIZE[1],
                                activation='relu', strides=STRIDES[1],
                                padding=PADDING, dilation_rate=DILATION_RATE[1],
                                kernel_initializer=KERNEL_INITIALIZER,
                                name='c_layer_three'),
            keras.layers.MaxPooling2D(pool_size=POOL_SIZE, padding=PADDING),
            keras.layers.Conv2D(FILTERS[2], KERNEL_SIZE[2],
                                activation='relu', strides=STRIDES[2],
                                padding=PADDING, dilation_rate=DILATION_RATE[2],
                                kernel_initializer=KERNEL_INITIALIZER,
                                name='c_layer_four'),
            keras.layers.Conv2D(FILTERS[2], KERNEL_SIZE[2],
                                activation='relu', strides=STRIDES[2],
                                padding=PADDING, dilation_rate=DILATION_RATE[2],
                                kernel_initializer=KERNEL_INITIALIZER,
                                name='c_layer_five'),
            keras.layers.MaxPooling2D(pool_size=POOL_SIZE, padding=PADDING),
            # End Convolution/Pooling, go to Dense
            keras.layers.Flatten(),
            keras.layers.Dense(128, activation='relu', name='h_layer_one'),
            keras.layers.Dropout(0.2, seed=RANDOM_SEED),
            keras.layers.Dense(64, activation='relu', name='h_layer_two'),
            keras.layers.Dropout(0.2, seed=RANDOM_SEED),
            keras.layers.Dense(10, activation='softmax', name='output_layer'),
        ]
    )
    return model

PROGRESS_BAR = 1
ONE_LINE_PER = 2
def compile_model(model):
    model.compile(
        optimizer='rmsprop',  # Default
        loss='binary_crossentropy',  # Cross entropy from class
        metrics=['accuracy']
    )
    return model

def train_model(model, X_train, Y_train, X_val, Y_val):
    history = model.fit(
        x=X_train,
        y=Y_train,
        validation_data=(X_val, Y_val),
        batch_size=128,
        epochs=12,
        verbose=ONE_LINE_PER
    )
    return model, history


def eval_model(model, X_test, Y_test):
    test_loss, test_accuracy = model.evaluate(x=X_test,
                                              y=Y_test,
                                              batch_size=128,
                                              verbose=1)
    return test_loss, test_accuracy
'''
