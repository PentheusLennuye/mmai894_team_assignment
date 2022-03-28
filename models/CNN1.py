from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense


class CNN1:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3)))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D())

        self.model.add(Conv2D(32, (3, 3), ))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D())

        self.model.add(Conv2D(64, (3, 3), ))
        self.model.add(Activation("relu"))
        self.model.add(MaxPooling2D())

        self.model.add(Flatten())
        self.model.add(Dense(128))
        self.model.add(Activation("relu"))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(20))  # output
        self.model.add(Activation("softmax"))

    def model_complie(self):
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def model_fitting(self, train_data, train_label, val_data, val_label):
        self.model.fit(train_data, train_label, epochs=30,
                            validation_data=(val_data, val_label))
