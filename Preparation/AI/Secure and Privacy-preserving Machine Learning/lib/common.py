"""From https://github.com/tf-encrypted/tf-encrypted/blob/master/examples/logistic/common.py"""

"""Provide classes to perform private training and private predictionn"""
import tensorflow as tf
import tf_encrypted as tfe


class DataOwner:
    """Contains code meant to be executed by a data owner Player."""

    def __init__(
        self, player_name, num_features, training_set_size, test_set_size, batch_size
    ):
        self.player_name = player_name
        self.num_features = num_features
        self.training_set_size = training_set_size
        self.test_set_size = test_set_size
        self.batch_size = batch_size
        self.train_initializer = None
        self.test_initializer = None

    @property
    def initializer(self):
        return tf.group(self.train_initializer, self.test_initializer)

    @tfe.local_computation
    def provide_training_data(self,x,y):
        """Preprocess training dataset

    Return single batch of training dataset
    """

        def norm(x, y):
            return tf.cast(x, tf.float32), tf.expand_dims(y, 0)

        train_set = (
            tf.data.Dataset.from_tensor_slices((x, y))
            .map(norm)
            .repeat()
            .shuffle(buffer_size=self.batch_size)
            .batch(self.batch_size)
        )

        train_set_iterator = train_set.make_initializable_iterator()
        self.train_initializer = train_set_iterator.initializer

        x, y = train_set_iterator.get_next()
        x = tf.reshape(x, [self.batch_size, self.num_features])
        y = tf.reshape(y, [self.batch_size, 1])

        return x, y

    @tfe.local_computation
    def provide_testing_data(self,x,y):
        """Preprocess testing dataset

    Return single batch of testing dataset
    """

        def norm(x, y):
            return tf.cast(x, tf.float32), tf.expand_dims(y, 0)

        test_set = (
            tf.data.Dataset.from_tensor_slices((x, y))
            .map(norm)
            .batch(self.test_set_size)
        )

        test_set_iterator = test_set.make_initializable_iterator()
        self.test_initializer = test_set_iterator.initializer

        x, y = test_set_iterator.get_next()
        x = tf.reshape(x, [self.test_set_size, self.num_features])
        y = tf.reshape(y, [self.test_set_size, 1])

        return x, y

class PredictionClient:
    """Contains methods meant to be executed by a prediction client."""

    def __init__(self, player_name, num_features):
        self.player_name = player_name
        self.num_features = num_features

    @tfe.local_computation
    def provide_input(self):
        return tf.random.uniform(
            minval=-0.5, maxval=0.5, dtype=tf.float32, shape=[1, self.num_features]
        )

    @tfe.local_computation
    def receive_output(self, result):
        return tf.print("Result on {}:".format(self.player_name), result)