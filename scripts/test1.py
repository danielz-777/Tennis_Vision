def greetings(name):
    print(f'Hi, {name}')

greetings('John Doe')
import tensorflow as tf
from tensorflow import keras
from keras.models import Model
from keras.layers import Dense
from keras.models import load_model
import csv
import cv2
import itertools
import numpy as np
import pandas as pd
import os
import sys
import tempfile
import tqdm

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import utils
#from data import BodyPart
pose_sample_rpi_path = os.path.join(os.getcwd(), 'examples/lite/examples/pose_estimation/raspberry_pi')
sys.path.append(pose_sample_rpi_path)
#from data import BodyPart
#from ml import Movenet
#movenet = Movenet('movenet_thunder')
import utils
#from data import BodyPart
from ml import Movenet
movenet = Movenet('movenet_thunder')
model = load_model('scripts/Tennis_Vision_Model.hdf5')



