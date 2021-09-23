import numpy as np
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Activation, BatchNormalization
from tensorflow.keras.layers import Flatten, GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.regularizers import l1_l2
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split


class PreprocessData:
    def __init__(self, valid_size, random_state):
        self.valid_size = valid_size
        self.random_state = random_state

    def _load_datasets(self):
        (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
        return train_images, train_labels, test_images, test_labels

    def scaled_pixels(self, images, labels):
        images = np.array(images/255., dtype=np.float32)
        labels = np.array(labels, dtype=np.float32)
        return images, labels

    def transform_ohe(self, labels):
        ohe_labels = to_categorical(labels)
        return ohe_labels

    def split_train_valid(self, train_images, train_ohe_labels):
        tr_images, tr_ohe_labels, val_images, val_ohe_labels = train_test_split(train_images, train_ohe_labels,
                                                                                test_size=self.valid_size,
                                                                                random_state=self.random_state)
        return tr_images, tr_ohe_labels, val_images, val_ohe_labels

    def preprocess_data(self):
        train_images, train_labels, test_images, test_labels = self._load_datasets()
        train_images, train_labels = self.scaled_pixels(train_images, train_labels)
        test_iamges, test_labels = self.scaled_pixels(test_images, test_labels)
        train_ohe_labels = self.transform_ohe(train_labels)
        test_ohe_labels = self.transform_ohe(test_labels)
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
    def create_model(verbose=False):
        size = CnnModel.input_size
        input_tensor = Input(shape=(size, size, 3))
        # Block 1
        x = Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', kernel_initializer='he_normal')(input_tensor)
        x = Conv2D(filters=32, kernel_size=3, padding='valid', activation='relu', kernel_initializer='he_normal')(x)
        x = MaxPooling2D(pool_size=2)(x)
        # Block 2
        x = Conv2D(filters=64, kernel_size=3, padding='same', kernel_initializer='he_normal')(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = MaxPooling2D(pool_size=2)(x)
        # Block 3
        x = Conv2D(filters=128, kernel_size=3, padding='same', kernel_initializer='he_normal')(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        x = MaxPooling2D(pool_size=2)(x)
        # Block 4
        x = Conv2D(filters=256, kernel_size=3, strides=2, padding='same', kernel_initializer='he_normal',
                   kernel_regularizer=l1_l2(l1=0.001, l2=0.001))(x)
        x = BatchNormalization()(x)
        x = Activation('relu')(x)
        # Classifier Layer
        x = GlobalAveragePooling2D()(x)
        x = Dropout(rate=0.3)(x)
        x = Dense(units=64, activation='relu')(x)
        x = Dropout(rate=0.2)(x)
        output = Dense(units=10, activation='softmax')(x)

        model = Model(inputs=input_tensor, outputs=output)
        if verbose:
            model.summary()
        return model

    @staticmethod
    def create_callbacks(checkpoint=False, reduce_lr=False, early_stopping=False):
        callbacks = []
        if checkpoint:
            mc_call = ModelCheckpoint(filepath='/Users/younghun/Desktop/models/weights.{epoch:02d}-{val_loss:.02f}.hdf5',
                                      save_best_only=True, save_weights_only=True, monitor='val_loss', mode='min',
                                      periods=3)
            callbacks.append(mc_call)
        if reduce_lr:
            lr_call = ReduceLROnPlateau(monitor='val_loss', mode='min', factor=0.2, patience=4, verbose=1)
            callbacks.append(lr_call)
        if early_stopping:
            ec_call = EarlyStopping(monitor='val_loss', mode='min', patience=6, verbose=1)
            callbacks.append(ec_call)

        if not callbacks:
            return None
        return callbacks


datasets = PreprocessData(valid_size=0.15, random_state=42)
tr_images, tr_ohe_labels, val_images, val_ohe_labels, test_images, test_ohe_labels = datasets.preprocess_data()

# CNN Model
cnn_model = CnnModel.create_model(verbose=True)
# compile
cnn_model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
# callbacks
callbacks = CnnModel.create_callbacks(checkpoint=1, reduce_lr=1, early_stopping=1)
# fit
train_hist = cnn_model.fit(x=tr_images, y=tr_ohe_labels, batch_size=64, epochs=20,
                           validation_data=(val_images, val_ohe_labels), callbacks=callbacks)
# Test
test_eval = cnn_model.evaluate(x=test_images, y=test_ohe_labels, batch_size=16)

print(f"Test data - test_loss:{test_eval[0]: .2f}, test_accuracy::{test_eval[1]*100: .2f}")



