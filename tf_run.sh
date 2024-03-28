#! /bin/bash
# from tutorial https://www.raspberrypi.com/documentation/computers/camera_software.html#post-processing-with-opencv
# model https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz
# labels https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_1.0_224_frozen.tgz

rpicam-hello --post-process-file object_classify_tf.json --lores-width 224 --lores-height 224