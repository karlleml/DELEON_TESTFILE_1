import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('diabetes.csv')
x_variables = dataset.iloc[:,0:8]
y_variable = dataset.iloc[:,8]
print(x_variables)
print(y_variable)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x_variables, y_variable, test_size =20, random_state = 10)

from keras import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(12, input_dim=8, activation = 'relu'))
model.add(Dense(15, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics =['accuracy'])
model.fit(x_variables, y_variable, epochs = 95, batch_size=25)
_, accuracy = model.evaluate(x_variables, y_variable)
print('Accuracy %.2f' %(accuracy*100))
model.summary()
