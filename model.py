import numpy as np 
import tensorflow as tf

def model(batch_size = 32):
	x = tf.placeholder(tf.float32, shape = (batch_size, 32, 32, 3), name = "input")
	y = tf.placeholder(tf.int32, shape = (batch_size,), name = "label")

	
