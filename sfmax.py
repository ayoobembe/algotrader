import compute_indicators as ci
import tensorflow as tf
from compute_indicators import get_trades
from compute_indicators import get_indicators

#get data
data_ = get_trades()
indicators_ = get_indicators()
training_set_data = data_[:,:int(data_.shape[1] * 0.75)].transpose()
training_set_indicators = indicators_[:,:int(indicators_.shape[1] * 0.75)].transpose()
testing_set_data = data_[:,int(data_.shape[1] * 0.75):].transpose()
testing_set_indicators = indicators_[:,int(indicators_.shape[1] * 0.75):].transpose()

#specify regression model
x = tf.placeholder("float",[None,6])#holds indicators
W = tf.Variable(tf.zeros([6,3]))      #converts indicators to buy/sell
b = tf.Variable(tf.zeros([3]))        #bias
y = tf.nn.softmax(tf.matmul(x,W)+b)

#Loss function:cross_entropy
y_ = tf.placeholder("float",[None,3])#holds correct answers
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#Graph-Op to initialize variables
init = tf.initialize_all_variables()

#Run training session
sess = tf.Session()
sess.run(init)
for i in range(276):
    batch_xs = training_set_indicators
    batch_ys = training_set_data
    sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})

#Evaluate the model
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print sess.run(accuracy, feed_dict={x: testing_set_indicators, y_:testing_set_data})




#print training_set_data.shape #3r*1104c
#print testing_set_data.shape  #3r*368c
#print training_set_indicators.shape #6r*1104c
#print testing_set_indicators.shape  #6r*368c
