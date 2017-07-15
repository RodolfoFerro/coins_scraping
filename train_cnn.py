import time
import os
import tensorflow as tf
import numpy as np
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

def mintToOneHot(cat):

    onehot = np.zeros(19)

    i = None
    i = 0 if cat == 'Emerita' else i
    i = 1 if cat == 'Caesaraugusta' else i
    i = 2 if cat == 'Colonia Patricia' else i
    i = 3 if cat == 'Rome' else i
    i = 4 if cat == 'Peloponnesus' else i
    i = 5 if cat == 'Samos' else i
    i = 6 if cat == 'Ephesus' else i
    i = 7 if cat == 'Pergamum' else i
    i = 8 if cat == 'Antioch' else i
    i = 9 if cat == 'Cyrene' else i
    i = 10 if cat == 'Caesareia in Cappadocia' else i
    i = 11 if cat == 'Commagene' else i
    i = 12 if cat == 'Carthage' else i
    i = 13 if cat == 'Gallia' else i
    i = 14 if cat == 'Vindobona' else i
    i = 15 if cat == 'Tarraco' else i
    i = 16 if cat == 'Narbo' else i
    i = 17 if cat == 'Alexandreia' else i
    i = 18 if cat == 'Asia Minor' else i

    if i is not None:
        onehot[i] = 1

    return onehot

def denToOneHot(cat):

    onehot = np.zeros(13)

    i = None
    i = 0 if cat == 'Quinarius' else i
    i = 1 if cat == 'Denarius' else i
    i = 2 if cat == 'As' else i
    i = 3 if cat == 'Aureus' else i
    i = 4 if cat == 'Quinarius aureus' else i
    i = 5 if cat == 'Dupondius' else i
    i = 6 if cat == 'Quadrans' else i
    i = 7 if cat == 'Sestertius' else i
    i = 8 if cat == 'Semis' else i
    i = 9 if cat == 'Cistophorus' else i
    i = 10 if cat == 'Drachma' else i
    i = 11 if cat == 'Didrachm' else i
    i = 12 if cat == 'Hemidrachm' else i

    if i is not None:
        onehot[i] = 1

    return onehot


if __name__ == '__main__':

    cnn = CNN()
    props, imgs = loadData('dataframe.csv', './images')

    cnn.setMintModel()
    
    train(cnn, input_x, input_y, 10000, 100, './')

