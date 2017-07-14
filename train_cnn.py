import time
import os
import tensorflow as tf
from cnn import CNN
from preprocessing import loadData


def train(cnn, input_x, input_y, nepochs, batch_size, check_dir):

    print('##############################')
    print('STARTING TRAINING...')
    print('##############################\n\n')

    for i in range(nepochs):

        start = time.time()
        _, train_loss = cnn.sess.run([cnn.train_op, cnn.loss], 
        	feed_dict={cnn.input_x: input_x, cnn.input_y: input_y})
        end = time.time() - start

        print('###################')
        print('Epoch {}'.format(i+1))
        print('###################\n\n')

        print('Learning rate: {}'.format(cnn.sess.run(cnn.learning_rate)))
        print('Time: {} s'.format(end))
        print('Loss: {}\n\n'.format(train_loss))

    if not os.path.exists(check_dir):
        os.makedirs(check_dir)
    ckpt = os.path.join(check_dir, cnn.id)
    cnn.saver = tf.train.Saver()
    cnn.saver.save(cnn.sess, ckpt)

if __name__ == '__main__':

    cnn = CNN()
    train(cnn, input_x, input_y, 10000, 100, './')