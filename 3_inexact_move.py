# move/sense loop:
#
#   Entropy is a measure of the amount of uncertainty in a system.
#
#   Entropy can be written as E = sum( -p[i] * log(p[i]) )
#   In a perfectly certain system ( p(Xi | Z) = 1 ), the entropy
#   evaluates to E = sum( -1 * log(1) ), or -1 * 0 = 0. All other
#   terms are 0 due to there being a zero probability of being in
#   that state.
#
#   Each "move" step increases uncertainty due to inexact motion,
#   which increases entropy. Each "sense" step reduces uncertainty
#   and therefore entropy. For a filter to converge, the "sense" step 
#   must reduce more entropy than the "move" step gains.

# prior uniform PDF
p = [0., 1., 0., 0., 0.]

# world data
world = ['green', 'red', 'red', 'green', 'green']

# measurement data
measurements = ['red', 'green']

pHit = 0.6 # coefficient to multiply matching sense data by
pMiss = 0.2 # coefficient to multiply non-matching sense data by

# sense function
# parameters:   p (prior belief) - distribution
#               Z (measurement) - scalar
def sense(p, Z):
	# initialize output PDF
	q = []
	# iterate through map (world values)
	for i in range(len(p)):
		# detect if sensed value matches world value
		hit = (Z == world[i])
		# multiply prior PDF by (hit * pHit) if hit, (!hit * pMiss) if miss
		q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
	# sum q for normalization
	s = sum(q)
	# normalize posterior
	for i in range(len(p)):
		q[i] /= s
	# return posterior
	return q

# move by U = 2
# p( X[i+1] | Xi ) = 0.2
# p( X[i+2] | Xi ) = 0.8
# p( X[i+3] | Xi ) = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# move function
# parameters:   p (prior belief) - distribution
#               U (inexact motion) - scalar (1D vector)
def move(p, U):
	# initialize output PDF
	q = []
	# assume world is cyclic, so shifts > world size will wrap
	U %= len(p)
	# iterate through world values
	for i in range(len(p)):
		# set posterior PDF to phase-shifted prior	
		q.append( pExact * p[i-U] + pOvershoot * p[i-U-1] + pUndershoot * p[i-U+1] )
	
	# normalize, just in case
	q = [float(i) / sum(q) for i in q]

	return q

# sense world
for i in range(len(measurements)):
	p = sense(p, measurements[i])

print(move(p,1))
