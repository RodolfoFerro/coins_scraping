import os
import numpy as np
import tensorflow as tf

class CNN(object):

    def __init__(self, name):

        self.defineCore()
        self.id = name
        self.defineCore()

    def setDenominationModel(self):

        W = self.set_variable('denomination_weights', [16*16*135, 13])
        b = self.set_variable('denomination_biases', [13])
        pred = tf.nn.bias_add(tf.matmul(self.final, W), b)

        loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=self.input_y, logits=pred))

        self.global_step = tf.Variable([0], dtype=tf.int32, trainable=False)
        self.learning_rate = tf.train.exponential_decay(
            0.01, self.global_step, 250, 0.8, staircase=True)

        self.trainer = tf.train.AdamOptimizer(self.learning_rate)
        self.gradients = self.trainer.compute_gradients(loss)
        self.clipped_gradients = [(tf.clip_by_norm(grad, 100), var) for grad, var in self.gradients]
        self.train_op = self.trainer.apply_gradients(self.clipped_gradients, global_step=self.global_step)

        self.sess = tf.Session()
        self.init = tf.global_variables_initializer()
        self.sess.run(self.init)

    def setMintModel(self):

        W = self.set_variable('mint_weights', [16*16*135, 19])
        b = self.set_variable('mint_biases', [19])
        pred = tf.nn.bias_add(tf.matmul(self.final, W), b)

        loss = tf.reduce_mean(
            tf.nn.softmax_cross_entropy_with_logits(labels=self.input_y, logits=pred))

        self.global_step = tf.Variable([0], dtype=tf.int32, trainable=False)
        self.learning_rate = tf.train.exponential_decay(
            0.01, self.global_step, 250, 0.8, staircase=True)

        self.trainer = tf.train.AdamOptimizer(self.learning_rate)
        self.gradients = self.trainer.compute_gradients(loss)
        self.clipped_gradients = [(tf.clip_by_norm(grad, 100), var) for grad, var in self.gradients]
        self.train_op = self.trainer.apply_gradients(self.clipped_gradients, global_step=self.global_step)

        self.sess = tf.Session()
        self.init = tf.global_variables_initializer()
        self.sess.run(self.init)

    def defineCore(self):

        self.input_x = tf.placeholder([None, 14400], dtype=tf.float32)
        self.input_y = tf.placeholder([None, 10], dtype=tf.float32)

        # Input layer
        input_layer = tf.reshape(self.input_x, [-1, 128, 128, 1])

        # Convolutional layers
        layer1 = self.convpool('layer1_{}'.format(self.id), [8, 8, 1, 135], input_layer)
        layer2 = self.convpool('layer2_{}'.format(self.id), [8, 8, 135, 135], layer1)
        layer3 = self.convpool('layer3_{}'.format(self.id), [8, 8, 135, 135], layer2)

        # Final layer
        with tf.variable_scope('endlayer_{}'.format(self.id)):
            in_flat = tf.reshape(layer3, [-1, 16*16*135])
            dense = tf.nn.relu(in_flat)
            fweights = self.set_variable('weights_endlayer_{}'.format(self.id), [16*16*135, 1], positive=True)
            fbias = self.set_variable('bias_endlayer_{}'.format(self.id), [1], positive=True)
            final = tf.matmul(dense, fweights)
            self.last = tf.nn.relu(tf.nn.bias_add(final, fbias))

    def predict(self, input_x):

        in_x = np.asarray(input_x).reshape(-1, self.nbits)
        pred = self.sess.run(self.predictions, feed_dict={self.input_x: in_x})
        return pred

    def load(self, name, check_dir):

        if not os.path.exists(check_dir):
            raise ValueError('The check_dir directory does not exist')
        ckpt = os.path.join(check_dir, name)
        self.saver = tf.train.Saver()
        self.saver.restore(self.sess, ckpt)

    def convpool(self, name, kernel, input_tensor):

        with tf.variable_scope(name) as scope:
            weights = self.set_variable('weights_{}'.format(scope.name), shape=kernel)
            biases = self.set_variable('biases_{}'.format(scope.name), shape=[kernel[3]])
            conv = tf.nn.conv2d(       
                input=input_tensor,
                filter=weights,
                strides=[1, 1, 1, 1],
                padding="SAME",
                name='preconv_{}'.format(scope.name))
            in_conv = tf.nn.relu(tf.nn.bias_add(conv, biases), name='conv_{}'.format(scope.name))
            in_pool = tf.nn.max_pool(
                value=in_conv,
                ksize=[1, 2, 2, 1],
                strides=[1, 2, 2, 1],
                padding='SAME',
                name=scope.name)

        return in_pool
            
    def set_variable(self, name, shape, positive=False):

        if positive == False:
            init = tf.truncated_normal_initializer(dtype=tf.float32, mean=0.0, stddev=0.5)
        else:
            init = tf.truncated_normal_initializer(dtype=tf.float32, mean=0.5, stddev=0.25)

        var = tf.get_variable(
            name=name,
            shape=shape,
            initializer=init,
            dtype=tf.float32,
            trainable=True)

        return var
