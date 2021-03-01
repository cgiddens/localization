# Bayes Theorem:
#
# P(A|B) = P(B|A)*P(A) / P(B)
# where
# P(B) = SUM_i(P(B|A_i)*P(A_i))

# Motion:

# P(X_i^t) = SUM_j(P(X_j^t-1)*P(X_i|X_j)
#
# simplified version: P(A) = SUM_B(P(A|B)*P(B)) -> Theorem of Total Probability
# -> this is a convolution. P(A|B) is the convolution kernel and P(B) is the prior distribution that is convolved
#    with the kernel.
#
# or,
#
# The probability of being in position X_i at time t is the sum for all j of the probability of being in position X_j at time t-1 multiplied
# by the probability of being in position X_i given prior position of X_j
#
# or,
#
# BEST EXPLANATION HERE:
#
# The probability of being in state X is the prior state belief distribution convolved with the movement distribution. In this context, the movement
# distribution is the kernel, which is overlaid on the prior distribution, multiplied pointwise and summed, then moved forward one cell and repeated
# for all grid cells.

