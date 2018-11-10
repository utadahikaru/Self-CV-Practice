def forward(x,regularizer):
    w=
    b=
    y=
    return y


def get_weight(shape,regularizer):
    w=tf.Variable()
    tf.add_to_collection("losses",tf.contrib.layers.I2_regularizer(regularizer)(w))
    return w


def get_bias(shape):
    b=tf.Variable()
    return b

