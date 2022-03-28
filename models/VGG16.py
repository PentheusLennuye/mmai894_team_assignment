import tensorflow as tf
from keras.applications.vgg16 import VGG16


class VGG:

    def __init__(self, train_data, val_data):
        self.vgg_model = VGG16(weights='imagenet', include_top=False)
        self.train_features = self.vgg_model.predict(train_data)
        self.test_features = self.vgg_model.predict(val_data)
        n_train, x, y, z = self.train_features.shape
        self.model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(x, y, z)),
            tf.keras.layers.Dense(256, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation=tf.nn.softmax)
        ])

    def model_complie(self):
        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def model_fitting(self, train_label, val_label):
        self.model.fit(self.train_features, train_label, epochs=30,
                            validation_data=(self.test_features, val_label))