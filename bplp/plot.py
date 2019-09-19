
# Adapted from code written by Remi Flamary
# <remi.flamary@unice.fr>
#
# License: MIT License

import numpy as np
import matplotlib.pylab as pl
from matplotlib import gridspec

def plot_joint_marginal(BayesLP, a, b, M, title=''):

    n = BayesLP.n
    interval = BayesLP.interval
    grid = np.linspace(interval[0], interval[1], n)

    na, nb = M.shape

    gs = gridspec.GridSpec(3, 3)

    ax1 = pl.subplot(gs[0, 1:])
    pl.plot(grid, b, 'r', label='Indifference condition')
    pl.title(title)

    ax2 = pl.subplot(gs[1:, 0])
    pl.plot(a, grid, 'b', label='Prior distribution')
    pl.gca().invert_xaxis()
    pl.gca().invert_yaxis()

    ax3 = pl.subplot(gs[1:, 1:])
    pl.imshow(M, interpolation='nearest')
    pl.axis('off')

    pl.tight_layout()
    pl.subplots_adjust(wspace=0.2, hspace=0.5)
