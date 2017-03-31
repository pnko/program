import tensorflow as tf
import os
from PIL import Image
image_dir="C:/kimhk/workspace/program/Python/IPNB/images.jpeg"
filename_list=[image_dir]

filename_queue = tf.train.string_input_producer(filename_list)
reader = tf.WholeFileReader()
key, value = reader.read(filename_queue)

image =tf.image.decode_png(value)

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    image, size = sess.run([image, tf.shape(image)])
    print(image)
    print(size)

    coord.request_stop()
    coord.join(threads)