import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
import numpy as np

class ResNet:

    def __init__(self, train_data):
        np.random.seed(seed=1997)
        # Number of estimators
        self.n_estimators = 10
        # Proporition of samples to use to train each training
        max_samples = 0.8
        max_samples *= train_data.shape[0]
        self.max_samples = int(max_samples)
        self.pretrained_model =  ResNet50(include_top=False, input_shape=(128, 128, 3), pooling='avg', classes=20,
                                    weights='imagenet')

    def define_model_and_complie(self):
        model_ensemble = tf.keras.Sequential([
            self.pretrained_model,
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(1024, activation=tf.nn.relu),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(20, activation=tf.nn.softmax)
        ])
        model_ensemble.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0007),
                               loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        return model_ensemble

    def model_fitting_prediction(self, train_data, train_label, val_data, val_label):
        predictions = []
        for i in range(self.n_estimators):
            # Train each model on a bag of the training data
            train_idx = np.random.choice(len(train_data), size=self.max_samples)
            model = self.define_model_and_complie()
            model.fit(train_data[train_idx], train_label[train_idx], batch_size=128, epochs=10,
                      validation_data=(val_data, val_label))
            predictions.append(model.predict(val_data))

        predictions = np.array(predictions)
        predictions = predictions.sum(axis=0)
        pred_labels = predictions.argmax(axis=1)
        return pred_labels