from tensorflow.keras import regularizers
import tensorflow as tf

class CNN2:

    def __init__(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3),
                                   kernel_regularizer=regularizers.l2(l=0.01)),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(l=0.01)),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
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
