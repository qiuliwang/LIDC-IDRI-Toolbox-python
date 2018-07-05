# -*- coding:utf-8 -*-
'''
 the idea of this script came from LUNA2016 champion paper.
 This model conmposed of three network,namely Archi-1(size of 10x10x6),Archi-2(size of 30x30x10),Archi-3(size of 40x40x26)

'''
import tensorflow as tf
from dataprepare import get_batch,get_train_and_test_filename
import random
import time
class model(object):

    def __init__(self,learning_rate,keep_prob,batch_size,epoch):
        print(" network begin...")
        self.learning_rate = learning_rate
        self.keep_prob = keep_prob
        self.batch_size = batch_size
        self.epoch = epoch

        self.cubic_shape = [[6, 20, 20], [30, 32, 32], [26, 40, 40]]

    def archi_2(self,input,keep_prob):
        with tf.name_scope("Archi-2"):
            # input size is batch_size x 32 x 32 x 30
            # 5x5x3 is the kernel size of conv1,1 is the input depth,64 is the number output channel
            w_conv1 = tf.Variable(tf.random_normal([3, 5, 5, 1, 64],stddev=0.001),dtype=tf.float32,name='w_conv1')
            b_conv1 = tf.Variable(tf.constant(0.01,shape=[64]),dtype=tf.float32,name='b_conv1')
            out_conv1 = tf.nn.relu((tf.nn.conv3d(input,w_conv1,strides=[1,1,1,1,1],padding='VALID')))
            out_conv1 = tf.nn.dropout(out_conv1,keep_prob)

            # max pooling ,pooling layer has no effect on the data size
            hidden_conv1 = tf.nn.max_pool3d(out_conv1,strides=[1,1,1,1,1],ksize=[1,1,2,2,1],padding='SAME')

            # after conv1 ,the output size is batch_size x 28 x 28 x 28 x 64([batch_size,in_deep,width,height,output_deep])
            w_conv2 = tf.Variable(tf.random_normal([3, 5, 5, 64, 64], stddev = 0.001), dtype=tf.float32,name='w_conv2')
            b_conv2 = tf.Variable(tf.constant(0.01, shape = [64]), dtype=tf.float32, name='b_conv2')
            out_conv2 = tf.nn.relu((tf.nn.conv3d(hidden_conv1, w_conv2, strides=[1, 1, 1, 1, 1], padding='VALID')))
            out_conv2 = tf.nn.dropout(out_conv2, keep_prob)

            # after conv2 ,the output size is batch_size x 26 x 24 x 24 x 64 ([batch_size,in_deep,width,height,output_deep])
            w_conv3 = tf.Variable(tf.random_normal([3 ,5, 5, 64, 64], stddev = 0.001), dtype=tf.float32,
                                  name='w_conv3')
            b_conv3 = tf.Variable(tf.constant(0.01, shape = [64]), dtype = tf.float32, name='b_conv3')
            out_conv3 = tf.nn.relu((tf.nn.conv3d(out_conv2, w_conv3, strides = [1, 1, 1, 1, 1], padding='VALID')))
            out_conv3 = tf.nn.dropout(out_conv3, keep_prob)

            out_conv3_shape = tf.shape(out_conv3)
            tf.summary.scalar('out_conv3_shape', out_conv3_shape[0])

            # after conv2 ,the output size is batch_size x 24 x 20 x 20 x 64([batch_size,in_deep,width,height,output_deep])
            # all feature map flatten to one dimension vector,this vector will be much long
            out_conv3 = tf.reshape(out_conv3,[-1,64*20*20*24])
            w_fc1 = tf.Variable(tf.random_normal([64*20*20*24,250],stddev=0.001),name='w_fc1')
            out_fc1 = tf.nn.sigmoid(tf.add(tf.matmul(out_conv3,w_fc1),tf.constant(0.001,shape=[250])))
            out_fc1 = tf.nn.dropout(out_fc1,keep_prob)

            out_fc1_shape = tf.shape(out_fc1)
            tf.summary.scalar('out_fc1_shape', out_fc1_shape[0])

            w_fc2 = tf.Variable(tf.random_normal([250, 2], stddev=0.001), name='w_fc2')
            out_fc2 = tf.nn.sigmoid(tf.add(tf.matmul(out_fc1, w_fc2), tf.constant(0.001, shape=[2])))
            out_fc2 = tf.nn.dropout(out_fc2, keep_prob)

            # w_sm = tf.Variable(tf.random_normal([2, 2], stddev=0.001), name='w_sm')
            # b_sm = tf.constant(0.001, shape=[2])
            # out_sm = tf.nn.softmax(tf.add(tf.matmul(out_fc2, w_sm), b_sm))
            return out_fc2



    def inference(self,npy_path,model_index,test_size,seed,train_flag=True):

        # some statistic index
        highest_acc = 0.0
        highest_iterator = 1

        train_filenames,test_filenames = get_train_and_test_filename(npy_path,test_size,seed)
        # how many time should one epoch should loop to feed all data
        times = len(train_filenames) // self.batch_size
        if (len(train_filenames) % self.batch_size) != 0:
            times = times + 1

        print("Training examples: ", len(train_filenames))
        # keep_prob used for dropout
        keep_prob = tf.placeholder(tf.float32)
        # take placeholder as input
        x = tf.placeholder(tf.float32, [None, self.cubic_shape[model_index][0], self.cubic_shape[model_index][1], self.cubic_shape[model_index][2]])
        x_image = tf.reshape(x, [-1, self.cubic_shape[model_index][0], self.cubic_shape[model_index][1], self.cubic_shape[model_index][2], 1])
        net_out = self.archi_2(x_image,keep_prob)

        saver = tf.train.Saver()  # default to save all variable,save mode or restore from path

        if train_flag:
            # softmax layer
            real_label = tf.placeholder(tf.float32, [None, 2])
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=net_out, labels=real_label)
            #cross_entropy = -tf.reduce_sum(real_label * tf.log(net_out))
            net_loss = tf.reduce_mean(cross_entropy)

            train_step = tf.train.MomentumOptimizer(self.learning_rate, 0.9).minimize(net_loss)

            prediction = tf.nn.softmax(net_out)
            correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(real_label, 1))
            accruacy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

            merged = tf.summary.merge_all()

            with tf.Session() as sess:
                #sess = tf_debug.LocalCLIDebugWrapperSession(sess)
                #sess.add_tensor_filter("has_inf_or_nan", tf_debug.has_inf_or_nan)
                sess.run(tf.global_variables_initializer())
                train_writer = tf.summary.FileWriter('./tensorboard/', sess.graph)
                # loop epoches
                for i in range(self.epoch):
                    epoch_start =time.time()
                    #  the data will be shuffled by every epoch
                    random.shuffle(train_filenames)
                    # times = 5
                    for t in range(times):
                        print(t, times)
                        batch_files = train_filenames[t*self.batch_size:(t+1)*self.batch_size]
                        batch_data, batch_label = get_batch(batch_files)
                        feed_dict = {x: batch_data, real_label: batch_label,
                                     keep_prob: self.keep_prob}
                        _,summary = sess.run([train_step, merged],feed_dict =feed_dict)
                        train_writer.add_summary(summary, i)
                        saver.save(sess, './ckpt/archi-2', global_step=i + 1)

                    epoch_end = time.time()
                    test_batch_file = []
                    testfileindex = random.sample(range(0, len(test_filenames)),16)
                    for index in testfileindex:
                        test_batch_file.append(test_filenames[index])
                    # test_batch_file = test_filenames[t * 16 : (t+1) * 16]
                    test_batch,test_label = get_batch(test_batch_file)
                    x10 = 0
                    x01 = 0
                    for label in test_label:
                        if label[0] == 1:
                            x10 += 1
                        else:
                            x01 += 1
                    print('percent: ', x10 / 16)
                    test_dict = {x: test_batch, real_label: test_label, keep_prob:self.keep_prob}
                    acc_test,loss = sess.run([accruacy,net_loss],feed_dict=test_dict)
                    print('accuracy  is %f' % acc_test)
                    print("loss is ", loss)
                    print(" epoch %d time consumed %f seconds"%(i,(epoch_end-epoch_start)))
                    if acc_test  > highest_acc:
                        highest_acc = acc_test
                        highest_iterator = i
            print("training finshed..highest accuracy is %f,the iterator is %d " % (highest_acc, highest_iterator))




























