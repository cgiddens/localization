p_C = 0.001
p_notC = 0.999

p_pos_given_C = 0.8
p_pos_given_notC = 0.1

# p( C | POS ) = p( X_i | Z )
# p_bar(C | POS)  = p(POS | C) * p(C)
#	-> p_bar(C | POS) = 0.8 * 0.001 = 0.0008
#	-> p_bar(notC | POS) = p(POS | notC) * p(notC) = 0.1 * 0.999 = 0.0999

# alpha = SUM{ p_bar } for all X = 0.0008 + 0.0999 = 0.1007 

# p(C | POS) = 1/alpha * p_bar(C | POS) = (1/0.1007) * 0.0008 = 0.007944

# coin flip question (fair)
# T -> accept
# H -> flip again, accept
# p( H ) after second flip:
#	p( H ) = sum_j( P( H) * P( H | T-1) ) for all previous states j
#			= 0.5*0.5 + 0.5*0 = 0.25

# loaded coin question
#
# fair coin 	-> p(H) = 0.5
# loaded coin 	-> p(H) = 0.1
#
# take random coin w/ 50% chance of being fair
# flip it
# observe H
# what is p(fair)?
#
# p(fair) = p(fair | H) = p(H | fair) * p(fair) / p(H)
#	-> p(fair | H) = p_bar(fair | H) / p(H)
#	-> get non-normalized answer first
# 		-> p_bar(fair | H) = p(H | fair) * p(fair) = 0.5 * 0.5 = 0.25
#	-> p(H) = sum( p_bar( fair | H ) for fair/not fair
#		-> p(H) = sum( 0.5*0.5, 0.1*0.5 ) = 0.25 + 0.05 = 0.3
#
#	-> p(fair | H) = 0.25 / 0.3 = 0.83333
