"""
from tensorflow.examples.tutorials.mnist import input_data
mnist= input_data.read_data_sets("MNIST_data/", one_hot=True)
print(mnist.train.labels[1])
print(mnist.train.images[1])


import tensorflow as tf
tf.convert_to_tensor(mnist.train.images).get_shape()
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
x = tf.placeholder("float", [None, 784])
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    if i % 100 == 0:
        print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

print("end")

"""

import tensorflow as tf
# CSV 파일 load
filename_queue = tf.train.string_input_producer(['test.csv'])
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)
record_defaults = [[1], [1], [1], [1], [1],[1],[1],[1],[1]]
col1, col2, col3, col4, col5, col6, col7, col8, col9 = tf.decode_csv(
    value, record_defaults=record_defaults)
# stack 묶기
print("aaa")
features = tf.stack([col1, col2, col3, col4,col5, col6, col7, col8, col9])
with tf.Session() as sess:
    example, label = sess.run([features, col5])
print('example:', example)
print('label:', label)