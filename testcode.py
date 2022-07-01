import numpy as np 
import pandas as pd 
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Convolution2D
from keras.layers.convolutional import MaxPooling2D
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from keras import backend as K

import shlex
    
shell_cmd = "testcode.py"
    
subprocess_cmd = shlex.split(shell_cmd)
subprocess.call(subprocess_cmd)
print(check_output(["ls", "C:/Users/USER/Desktop/School/DataScie/minst"]).decode("utf8"))

