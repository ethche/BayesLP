# BayesLP

This project uses the connection made between optimal transport and Bayesian Persuasion in  Kolotilin (2018) to identify and visualize optimal information mechanisms. Please see the slides for details concerning the communication game of the paper.

The linear programming approach in this paper, under certain circumstances, allows us to explicitly compute optimal mechanisms as the solution of a transportation problem in situations where concavification does not easily generate a concrete solution.

In the standard optimal transport setting, the objective is to minimize the cost from moving the mass of one probability measure to another. Specifically, to minimize a cost functional of a joint distribution, in which the marginal distributions in the source and target spaces match the source and target distributions.

In the Bayesian Persuasion setting, the sender is choosing a joint distribution (implicitly a Blackwell experiment) between states and messages, such that the marginal distribution with respect to the state space is the prior distribution. In addition, the projection of the joint distribution on the message space must satisfy an incentive compatibility or an "obedience" constraint in terms of the receiver's utility (as messages in the Kolotilin model are interpreted as action recommendations).

As an illustration of the usefulness of the connection with optimal transport, here is the optimal mechanism when the sender's (state-independent) utility is the square of the message:

![optional caption text](figures/plt_primal_mechanism_square_util_grid_100.png)
