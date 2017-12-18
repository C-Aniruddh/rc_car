import cv2
import numpy as np
import glob
import keras.backend
from keras.layers import Flatten, Dense, Dropout, Lambda, Convolution2D, Cropping2D, Conv2D, Conv1D, Reshape
from keras.callbacks import EarlyStopping
from keras.models import Sequential
import matplotlib.pyplot as plt

print('Loading training data...')
e0 = cv2.getTickCount()

# load training data
image_array = np.zeros((1, 38400))
label_array = np.zeros((1, 4), 'float')
training_data = glob.glob('training_data/*.npz')

for single_npz in training_data:
    with np.load(single_npz) as data:
        print(data.files)
        train_temp = data['train']
        train_labels_temp = data['train_labels']
        print(train_temp.shape)
        print(train_labels_temp.shape)
    image_array = np.vstack((image_array, train_temp))
    label_array = np.vstack((label_array, train_labels_temp))

train = image_array[1:, :]
train_labels = label_array[1:, :]
print(train.shape)
print(train_labels.shape)

show_images = False
export_images = False
should_train = True


def show_image(sample, delay=200):
    sample = sample.reshape((120, 320)).astype(np.uint8)
    cv2.imshow('image', sample)
    cv2.waitKey(delay=delay)


if show_images:
    for sample in train:
        show_image(sample)

if export_images:
    for i, sample in enumerate(train):
        sample = sample.reshape((120, 320)).astype(np.uint8)
        cv2.imwrite('export/' + str(i) + '.png', sample)

if not should_train:
    exit('should not train')

e00 = cv2.getTickCount()
time0 = (e00 - e0) / cv2.getTickFrequency()
print('Loading image duration = '.format(time0))

# set start time
e1 = cv2.getTickCount()

model = Sequential([
    Reshape((320, 120), input_shape=(train[0].shape)),
    # Conv2D(24, kernel_size=(3, 3), strides=(3, 3), activation='relu', input_shape=input_shape),
    Conv1D(24, kernel_size=3, strides=3, activation='relu'),
    Dropout(0.5),
    # Conv2D(36, kernel_size=(3, 3), strides=(3, 3), activation='relu'),
    Conv1D(32, kernel_size=3, strides=3, activation='relu'),
    Dropout(0.5),
    Conv1D(48, kernel_size=3, strides=3, activation='relu'),
    Flatten(),
    Dense(10),
    Dense(4)
])

model.compile(loss='mse', optimizer='adam')

#early_stopping = EarlyStopping(monitor='val_loss', patience=2)
history = model.fit(train, train_labels, nb_epoch=120, validation_split=0.2)

model.save('model.h5')

# plot the model history
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.savefig('history.png')

# try to avoid 'NoneType' object has no attribute 'TF_DeleteStatus' error
keras.backend.clear_session()
