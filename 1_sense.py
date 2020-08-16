# prior uniform PDF
p = [0.2, 0.2, 0.2, 0.2, 0.2]

# world data
world = ['green', 'red', 'red', 'green', 'green']

# measurement data
measurements = ['red', 'green']

pHit = 0.6 # coefficient to multiply matching sense data by
pMiss = 0.2 # coefficient to multiply non-matching sense data by

# sense function
# parameters:   p (prior distribution)
#               Z (measurement)
def sense(p, Z):
	# initialize output PDF
	q = []
	# iterate through map (world values)
	for i in range(len(p)):
		# if match, hit = 1
		hit = (Z == world[i])
		# add (hit * pHit), or, if not hit, (!hit * pMiss)
		q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
	# sum q for normalization
	s = sum(q)
	# normalize
	for i in range(len(p)):
		q[i] /= s
	return q

# sense for all measurements
for i in range(len(measurements)):
	p = sense(p, measurements[i])

print(p)
