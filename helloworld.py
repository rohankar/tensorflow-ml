import tensorflow as tf

hello = tf.constant('Hello World!')

# Start tf session
sess = tf.Session()

# Run the op
print sess.run(hello)
