# primal methods
import numpy as np
import scipy.optimize as opt

# primal solver
def bayes_primal(program):
    """
    Sets up the primal program given the parameters specified in program
    INPUT
        program (BayesLP) class instance that contains parameters of the
            problem.
    RETURNS
        constraints (dict) contains the constraints of the Bayes LP problem,
            which are the required marginal distributions of the optimal mechanism.
            prior (n x 1 array) the prior distribution of the states.
            ic_constraint (n x 1 array) an array of 0s indicating the receiver's
                expected utility in each state
        primal (dict) contains results of the primal LP:
            mechanism (n x n array) joint probability distribution between states
                and messages.
            value_mat (n x n array) the expected utility obtained by the sender
                under the optimal mechanism.
        dual (dict) contains results of the dual LP:
            
    """

    # load program and set up the grid
    n = program.n
    interval = program.interval
    grid = np.linspace(interval[0], interval[1], n)

    # vectorize functions
    prior_vec = np.vectorize(program.prior)
    u_vec     = np.vectorize(program.u)
    g_vec     = np.vectorize(program.g)
    v_vec     = np.vectorize(program.v)

    ## constraint realizations
    # Bayes-plausibility constraint
    bayes_b = prior_vec(grid)
    # normalize prior distribution
    if sum(bayes_b) != 1.:
        bayes_b = np.divide(bayes_b, sum(bayes_b))
    # incentive compatibility constraint
    ic_b = np.zeros(n)
    # concatenate constraint realizations
    b = np.concatenate((bayes_b, ic_b), axis = 0)

    # sender expected utility matrix
    V_mat = np.ndarray(shape = (n,n))

    # create utility matrix from the sender's utility function
    for j in range(n):
        V_mat[:,j] = v_vec(grid,grid[j])
    # reshape to an n^2 array, the cost vector in the LP
    V = V_mat.reshape((n**2))
    # negative, so that linprog will return a maximum
    V = -V

    # The A matrix, defines projections on S and M
    ones = np.ones(n)
    ones_T = ones.reshape((n,1))

    # the rows of the transpose of the A matrix correspond
    # with the projection on state space S
    row_proj = np.kron(np.eye(n), ones_T)

    # the columns of the transpose of the A matrix correspond with
    # the projection of the mechanism times the tilde utility function on
    # the message space M.
    col_proj = []
    for i in range(n):
        u_tilde_si = u_vec(grid[i], grid) * g_vec(grid[i], grid)
        u_si_mat = np.diag(u_tilde_si)

        if i == 0:
            col_proj = u_si_mat
        else:
            col_proj = np.vstack((col_proj, u_si_mat))

    # stack the row space projection and the column space projection
    # horizontally. Then take the transpose.
    A_T = np.hstack((row_proj, col_proj))
    A   = A_T.T

    # Solve with linprog
    bp_lin_prog = opt.linprog(V, A_eq = A, b_eq = b)

    # recover joint probability distribution
    phi = bp_lin_prog.x.reshape((n,n))
    # normalize
    phi = np.divide(phi, phi.sum())

    value_matrix = -V
    value_matrix = value_matrix.reshape((n, n))

    primal = {"mechanism": phi,
               "prior": bayes_b,
               "ic_constraint": ic_b,
               "value_mat": value_matrix}

    return(outcome)

# Dual solver
#def bayes_dual(program):
