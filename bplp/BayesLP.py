# problem
import numpy as np
from scipy.stats import norm

class BayesLP:

    def __init__(self):

        # Number of points in the grid
        self.n_grid = 10
        self.interval = [0, 1]

        # Receiver's utility function
        self.receiver_util = lambda s, r: s - r
        # Receiver's private information distribution
        self.private_info = lambda s, r: 1

        # Sender's utility function
        self.sender_util = lambda s, m: m**2

        # Prior distribution
        self.prior = lambda s: norm.pdf(s)
