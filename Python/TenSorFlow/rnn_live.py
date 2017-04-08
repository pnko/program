import tensorflow as tf

CONSTANT = tf.app.flags

CONSTANT.DEFINE_integer("samples", 1000, "simulation data samples")
CONSTANT.DEFINE_integer("hidden", 5, "hidden layers in rnn")
CONSTANT.DEFINE_integer("vec_size", 1, "input vector size into rnn")
CONSTANT.DEFINE_integer("batch_size", 10, "minibatch size for training")
CONSTANT.DEFINE_integer("state_size", 15, "state size in rnn")
CONSTANT.DEFINE_integer("recurrent", 5, "recurrent step")
CONSTANT.DEFINE_float("learning_rate", 0.01, 'learning rate for optimizer')
CONST = CONSTANT.FLAGS


class rnn_live(object):


    def __init__(self):
        self._gen_sim_data()

    def run(self):
        self._initialize()
        print(self._run_session())
        self._close_session()

    @classmethod
    def _run_session(cls):
        output = cls.sess.run(cls.ts_y)
        return output

    @classmethod
    def _initialize(cls):
        cls.sess = tf.Session()

    @classmethod
    def _close_session(cls):
        cls.sess.close()

    @classmethod
    def _gen_sim_data(cls):
        ts_x = tf.constant([i for i in range(CONST.samples+1)], dtype=tf.float32)
        cls.ts_y = tf.sin(ts_x * 0.1)

        sp_batch = (int(CONST.samples/CONST.hidden), CONST.hidden, CONST.vec_size)
        cls.batch_input = tf.reshape(cls.ts_y[:-1], sp_batch)
        cls.batch_label = tf.reshape(cls.ts_y[1:], sp_batch)




def main(_):
    #print(CONST.test_int)
    # TF Print
    #tf.Print([graph_end_point1, graph_end_point2], what_you_print, "message you wate")
    run = rnn_live()
    run.run()


if __name__ == "__main__":
    tf.app.run()
