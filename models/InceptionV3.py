import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3

class Inception:

    def __init__(self):
        input_tensor = Input(shape=(128, 128, 3))

        inceptionv3 = InceptionV3(input_tensor=input_tensor, weights='imagenet', include_top=False)
        self.model = tf.keras.Sequential([
            inceptionv3,
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(1024, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation=tf.nn.softmax)
        ])

    def model_complie(self):
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def model_fitting(self, train_data, train_label, val_data, val_label):
        self.model.fit(train_data, train_label, epochs=20, batch_size=128,
                            validation_data=(val_data, val_label))
