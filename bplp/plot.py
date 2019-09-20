
# Adapted from code written by Remi Flamary
# <remi.flamary@unice.fr>
#
# License: MIT License

import numpy as np
import matplotlib.pylab as pl
from matplotlib import gridspec

def plot_primal_joint_marginal(solved_program, title=''):
    """
    Plots the primal mechanism, which is a joint probability distribution
    between states and messages. Plots the marginals, which include the prior
    distribution and the incentive compatibility constraint of the receiver
    for all messages.
    INPUT
        solved_program (dict) this is the output of "bayes_lp_solver". Contains
            the parameters along with the primal and dual solutions
    RETURNS

    """

    # Set up grid for the state and message spaces
    n        = solved_program["n_grid"]
    interval = solved_program["interval"]
    grid     = np.linspace(interval[0], interval[1], n)

    # Dimensions from the primal solution
    na, nb = solved_program["primal"].shape

    gs = gridspec.GridSpec(3, 3)

    # Plot the IC constraint
    ax1 = pl.subplot(gs[0, 1:])
    pl.plot(grid, solved_program["ic_constraint"], 'r', label='Indifference condition')
    pl.title(title)

    # Plot the prior constraint
    ax2 = pl.subplot(gs[1:, 0])
    pl.plot(solved_program["prior_constraint"], grid, 'b', label='Prior distribution')
    pl.gca().invert_xaxis()
    pl.gca().invert_yaxis()

    # Plot heatmap of the primal mechanism
    ax3 = pl.subplot(gs[1:, 1:])
    pl.imshow(solved_program["primal"], interpolation='nearest')
    pl.axis('off')

    pl.tight_layout()
    pl.subplots_adjust(wspace=0.2, hspace=0.5)
