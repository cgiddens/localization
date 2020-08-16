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

# move function
# parameters:   p (prior belief) - distribution
#               U (exact motion) - scalar / 1D vector
def move(p, U):
	# initialize output PDF
	q = []
	# assume world is cyclic, so shifts > world size will wrap.
    # take modulus of len(p), since everything before it will
    # leave robot in the same place.
	U %= len(p)
	# iterate through world values
	for i in range(len(p)):
		# set posterior PDF to phase-shifted prior	
		q.append(p[i-U])
	return q

# sense world
for i in range(len(measurements)):
	p = sense(p, measurements[i])

print(move(p,1))
