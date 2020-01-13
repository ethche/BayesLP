# Adapted from code written by Remi Flamary
# <remi.flamary@unice.fr>
#
# License: MIT License

import numpy as np
import matplotlib.pylab as pl
from matplotlib import gridspec

def plot_primal_joint_marginal(solved_program, dir, title = ''):
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
    na, nb = solved_program["mechanism"].shape

    gs = gridspec.GridSpec(4, 4)

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

    # set ticks:
    ticks    = [i for i in range(0, n, int(0.2 * n))]
    tick_lab = [round((1/n) * i,1) for i in range(0, n, int(0.2 * n))]

    ax3.set_xticks(ticks)
    ax3.set_xticklabels(tick_lab)
    ax3.set_yticks(ticks)
    ax3.set_yticklabels(tick_lab)

    pl.imshow(solved_program["mechanism"], interpolation='nearest')

    pl.tight_layout()
    pl.subplots_adjust(wspace=0.1, hspace=0.8)
    pl.savefig(dir, dpi = 300)

    return pl
