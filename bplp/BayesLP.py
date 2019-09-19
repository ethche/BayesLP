# problem
import numpy as np
from scipy.stats import norm

class BayesLP:

    def __init__(self):

        # Number of points in the grid
        self.n = 10
        self.interval = [0, 1]

        # receiver utility function and conditional probability density
        self.u = lambda s, r: s - r
        self.g = lambda s, r: 1

        # sender utility function
        self.v = lambda s, m: m**2

        # density of prior distribution
        self.prior = lambda s: norm.pdf(s)
