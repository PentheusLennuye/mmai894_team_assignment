import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50


class ResNet:

    def __init__(self):
        pretrained_model = ResNet50(include_top=False, input_shape=(128, 128, 3), pooling='avg', classes=20,
                                    weights='imagenet')
        self.model = tf.keras.Sequential([
            pretrained_model,
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(1024, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation=tf.nn.softmax)
        ])

    def model_complie(self):
        self.model.compile(optimizer= tf.keras.optimizers.Adam(learning_rate=0.0007),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

    def model_fitting(self, train_data, train_label, val_data, val_label):
        self.model.fit(train_data, train_label, epochs=20, batch_size=128,
                            validation_data=(val_data, val_label))