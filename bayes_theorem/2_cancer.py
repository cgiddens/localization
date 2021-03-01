# Bayes Theorem:
#
# P(A|B) = P(B|A)*P(A) / P(B)
# where
# P(B) = SUM_i(P(B|A_i)*P(A_i))

# Problem:

# C = cancer
# pos/neg = test result

# Givens:
# p(C) = 0.001
# p(!C) = 0.999
# p(pos|C) = 0.8
# p(pos|!C) = 0.1

# find p(C|pos)

# Sol'n:

# p(C|pos) = p(pos|C)*p(C) / p(pos)
#          = 0.8 * 0.001 / p(pos)
# p(pos) = p(pos|C)*p(C) + p(pos|!C)*p(!C)
#        = 0.8*0.001 + 0.1*0.999 = 0.1007

# p(C|pos) = 0.8 * 0.001 / 0.1007 = 0.007944
