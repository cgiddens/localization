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
# Problem: Coin Flip
#
# Givens:
# P(T) = P(H) = 0.5
# T -> accept
# H -> flip again, accept
#
# What is p(H)?
#
# Sol'n:
#
# p(H) = SUM_B(P(H|B)*P(B))
#      = P(H|H)*P(H) + P(H|T)*P(T)
#      = 0.5*0.5 + 0*0.5
#      = 0.25
#
# =========================================
#
# Problem: 2 Coin Flip
#
# Givens:
# fair coin: P(H|f) = 0.5, P(T|f) = 0.5
# loaded coin: P(H|l) = 0.1, P(T|l) = 0.9
# take random coin: p(f) = p(h) = 0.5
#
# Grab coin, flip it, observe H. What is the probability the coin was fair, or p(f|H)?
#
# Sol'n:
#
# Start w/ Bayes Theorem.
# -> need p(f|H).
# -> measurement: H. State: f
# p(f|H) = p(H|f)*p(f) / p(H)
#        = 0.5*0.5 / p(H)
#
# need p(H).
#
# Use Theorem of Total Probability:
# -> need p(H)
# -> state: H. Prior: fair/loaded
# p(H) = SUM_fl(p(H|B)*p(B))
#      = p(H|f)*p(f) + p(H|l)*p(l)
#      = 0.5*0.5 + 0.1*0.5
#      = 0.3
#
# -> p(f|H) = 0.5*0.5 / 0.3 = 0.833333
#
# ALTERNATIVE METHOD:
#
# find non-normalized p(f|H), or p_(f|H)
#
# p(f|H) = 1/a * p_(f|H)
#
# a = normalization coefficient
#   = SUM_fl(p(H|B)*p(B))
#   = p(H|f)*p(f) + p(H|l)*p(l) = 0.5*0.5 + 0.1*0.5 = 0.3
# p_(f|H) = p(H|f)*p(f) = 0.5*0.5 = 0.25
#
# -> p(f|H) = 1/.3 * 0.25 = 0.8333333
