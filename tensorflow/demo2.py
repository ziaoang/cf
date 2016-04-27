import sys

import tensorflow as tf
import numpy as np
import random

x = tf.placeholder(tf.float32, [None, 9923])
y_ = tf.placeholder(tf.float32, [None, 1])

W = tf.Variable(tf.random_normal([9923, 1]))
b = tf.Variable(tf.random_normal([1]))

y = tf.matmul(x, W) + b

cost = tf.square(y - y_)

sgd = tf.train.GradientDescentOptimizer(0.5).minimize(-cost)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)


pool = []


cnt = 0
for line in open("../rowcol/train.rc2"):
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt)

    # if random.random() < 0.99999:
    #     continue

    t = line.strip().split(" ")

    yFea = np.zeros((1,1))
    yFea[0][0] = float(t[0])

    xFea = np.zeros((1, 9923))
    for entry in t[1:]:
        tt = entry.split(":")
        index = int(tt[0]) - 1
        value = float(tt[1])
        xFea[0][index] = value

    pool.append([xFea, yFea])

    # print("w + b")
    # print(sess.run(W), sess.run(b))

    # print("cost")
    # print(sess.run(cost, feed_dict = {x: xFea, y_: yFea}))

    # sess.run(sgd, feed_dict = {x: xFea, y_: yFea})


# err = 0
# cnt = 0
# for line in open("../rowcol/test.rc2"):
#     cnt += 1
#     if cnt % 1000 == 0:
#         print(cnt)

#     t = line.strip().split(" ")

#     yFea = np.zeros((1,1))
#     yFea[0][0] = float(t[0])

#     xFea = np.zeros((1, 9923))
#     for entry in t[1:]:
#         tt = entry.split(":")
#         index = int(tt[0]) - 1
#         value = float(tt[1])
#         xFea[0][index] = value

#     err += sess.run(cost, feed_dict = {x: xFea, y_: yFea})
#     break

# print(err)


