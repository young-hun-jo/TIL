import numpy as np
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, GlobalAveragePooling2D, Activation, BatchNormalization, Dropout, Flatten, Dense
from tensorflow.keras.models import Model


class PreprocessData:
    def __init__(self, valid_size, random_state, scaling=False):
        self.valid_size = valid_size
        self.random_state = random_state
        self.scaling = scaling

    def load_datasets(self):
        (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
        return train_images, train_labels, test_images, test_labels

    def scaled_pixels(self, images, labels):
        if self.scaling:
            images = np.array(images / 255.0, dtype=np.float32)
        else:
            images = np.array(images, dtype=np.float32)
        labels = np.array(labels, dtype=np.float32)
        return images, labels

    def transform_ohe(self, labels):
        ohe_labels = to_categorical(labels)
        return ohe_labels

    def split_train_valid(self, train_images, train_ohe_labels):
        tr_images, val_images, tr_ohe_labels, val_ohe_labels = train_test_split(train_images, train_ohe_labels,
                                                                                test_size=self.valid_size,
                                                                                random_state=self.random_state)
        return tr_images, val_images, tr_ohe_labels, val_ohe_labels

    def preprocess_data(self):
        # load dataset
        train_images, train_labels, test_images, test_labels = self.load_datasets()
        # convert to float32(not scaling)
        train_images, train_labels = self.scaled_pixels(train_images, train_labels)
        test_images, test_labels = self.scaled_pixels(test_images, test_labels)
        # transform labels into One-hot encoding
        train_ohe_labels = self.transform_ohe(train_labels)
        test_ohe_labels = self.transform_ohe(test_labels)
        # split train, valid data
        tr_images, val_images, tr_ohe_labels, val_ohe_labels = self.split_train_valid(train_images, train_ohe_labels)
        # check shape
        print('Train:', tr_images.shape, tr_ohe_labels.shape)
        print('Valid:', val_images.shape, val_ohe_labels.shape)
        print('Test:', test_images.shape, test_ohe_labels.shape)

        return tr_images, tr_ohe_labels, val_images, val_ohe_labels, test_images, test_ohe_labels


class CnnModel:
    input_size = 32

    @classmethod
    def change_input_size(cls, input_size):
        CnnModel.input_size = input_size

    @staticmethod
    def create_model(verbose=True):
        size = CnnModel.input_size
        input_tensor = Input(shape=(size, size, 3))
        # Block1
        x = Conv2D(filters=32, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu')(
            input_tensor)
        x = Conv2D(filters=32, kernel_size=3, padding='same', kernel_initializer='he_normal')(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = MaxPooling2D(pool_size=2)(x)
        # Block2
        x = Conv2D(filters=64, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu')(x)
        x = Conv2D(filters=64, kernel_size=3, padding='same', kernel_initializer='he_normal')(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = MaxPooling2D(pool_size=2)(x)
        # Block3
        x = Conv2D(filters=128, kernel_size=3, padding='valid', kernel_initializer='he_normal', activation='relu')(x)
        x = Conv2D(filters=128, kernel_size=3, padding='same', kernel_initializer='he_normal')(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = MaxPooling2D(pool_size=2)(x)
        # Block4
        x = Conv2D(filters=256, kernel_size=3, strides=2, padding='same', kernel_initializer='he_normal')(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        # Classfier Layer
        x = Flatten()(x)
        x = Dropout(rate=0.4)(x)
        x = Dense(units=256, kernel_initializer='he_normal', activation='relu')(x)
        x = Dropout(rate=0.3)(x)
        x = Dense(units=64, kernel_initializer='he_normal', activation='relu')(x)
        output = Dense(units=10, activation='softmax')(x)

        model = Model(inputs=input_tensor, outputs=output)
        if verbose:
            model.summary()

        return model