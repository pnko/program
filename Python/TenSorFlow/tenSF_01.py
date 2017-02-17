"""
#01. 텐서플로 실행 테스트
import tensorflow as tf

a=tf.placeholder("float")

b=tf.placeholder("float")

y = tf.mul(a,b)

sess= tf.Session()

print( sess.run(y, feed_dict={a: 3, b: 9}))
"""

#02. Random 함수를 이용한 단순회귀 실습
import numpy as np
num_points = 1000
vectors_set = []

for i in range(num_points):
    x1 = np.random.normal(0.0, 0.55)
    y1 = x1 * 0.1 +0.3 + np.random.normal(0.0, 0.03)
    vectors_set.append([x1, y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

import matplotlib.pyplot as plt

plt.plot(x_data, y_data, 'ro')
plt.show()


#03. 선형회귀분석
import  tensorflow as tf

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data +b

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#실행부
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(8) :
    sess.run(train)
    print(step, sess.run(W), sess.run(b),  sess.run(loss))
    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, sess.run(W) * x_data + sess.run(b))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


