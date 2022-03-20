#!/usr/bin/env python3
'''
Base Model for MMAI894 "Cake Detector"
'''
import numpy as np
import matplotlib.pyplot as plt

import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Dense, Dropout, Conv2D, MaxPooling2D,
                                     Flatten)