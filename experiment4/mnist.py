import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras import layers
from keras import models

if __name__ == "__main__":
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()
    X_train = X_train.reshape([60000, 784])
    X_test = X_test.reshape([10000, 784])
    X_train = X_train.astype(np.float32)
    X_test = X_test.astype(np.float32)

    X_train = X_train / 255
    X_test = X_test / 255

    train_labels = np_utils.to_categorical(Y_train)
    test_labels = np_utils.to_categorical(Y_test)

    model = models.Sequential()
    model.add(layers.Dense(128, input_shape=(784,), activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))
    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, train_labels, epochs=200, batch_size=128, verbose=1, validation_split=0.2)

    test_loss, test_acc = model.evaluate(X_test, test_labels, verbose=1)

    print(test_loss, test_acc)
