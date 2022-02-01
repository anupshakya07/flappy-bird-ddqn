import tensorflow as tf
import cv2
import sys

from keras.optimizers import Adam
from tensorflow.keras import layers, models
sys.path.append("game/")

import game.flappy_bird as game
import random
import numpy as np

GAME = 'bird'
N_ACTIONS = 2
GAMMA = 0.99
OBSERVE = 100000.
EXPLORE = 2000000.
FINAL_EPSILON = 0.0001
INITIAL_EPSILON = 0.0001
REPLAY_MEMORY = 50000
BATCH = 32
FRAME_PER_ACTION = 1


def createNeuralNetwork():
    # model = models.Sequential()

    # model.add(layers.Conv2D(32, (8, 8, 4)))

    input_pixels = layers.Input(shape=(80, 80, 4))
    conv1_op = conv_block(inp=input_pixels, filters=32, kernel_size=(8, 8), strides=4, pool=True)
    conv2_op = conv_block(inp=conv1_op, filters=64, kernel_size=(4, 4), strides=2, pool=False)
    conv3_op = conv_block(inp=conv2_op, filters=64, kernel_size=(3, 3), strides=1, pool=False)
    flattened_op = layers.Flatten()(conv3_op)
    dense_op = layers.Dense(units=512, activation='relu', use_bias=True,
                             bias_initializer=tf.keras.initializers.constant(0.01))(flattened_op)
    readout = layers.Dense(units=2, use_bias=True, bias_initializer=tf.keras.initializers.constant(0.01))(dense_op)

    model = models.Model(inputs=input_pixels, outputs=[readout])
    model.compile(optimizer=Adam(lr=0.001), loss={'output': 'mse'}, metrics={'output': 'accuracy'})

    return model, input_pixels, readout, dense_op


def conv_block(inp, filters=64, kernel_size=(8, 8), strides=4, pool=True):
    _ = layers.Conv2D(filters=filters, kernel_size=kernel_size, strides=strides, activation='relu', use_bias=True,
                      bias_initializer=tf.keras.initializers.constant(0.01), padding="SAME")(inp)
    if pool:
        _ = layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="SAME")(_)

    return _


def trainNetwork(model, input_pixels, readout, dense_op):

    return False


def start_main():
    model, input_pixels, readout, dense_op = createNeuralNetwork()
    trainNetwork(model, input_pixels, readout, dense_op)


if __name__ == "__main__":
    start_main()