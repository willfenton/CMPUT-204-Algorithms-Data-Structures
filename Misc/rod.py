# Rod Cutting algorithm implemented in Python 3
# March 11th 2019

## The initial method, naive_cut_rod, operates in exponential O(2^n) time
## The memoized method, memoized_cut_rod, operators in O(n^2) time

## List of prices 
p=[0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 33, 35, 37, 41, 48, 55, 61, 62, 64, 69, 72, 78, 81, 90, 91, 93, 101, 105, 109, 110]

def naive_cut_rod(p, n):
	if n==0:
		return 0
	q=-32767
	for i in range(1, n+1):
		q=max(q, p[i]+naive_cut_rod(p, n-i))
	return q
#for j in range(21):
	## feel free to change this constant around
	## if you set it to j=11, you get page 362 of CLRS
	## if you set it to j=21, you get a funny answer
	## if you set it to anything higher, it'll start lagging 
	#print(naive_cut_rod(p, j))

def memoized_cut_rod(p, n):
	r=[-32767]*(n+1)
	return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
	if r[n]>=0:
		return r[n]
	if n==0:
		q=0
	else:
		q=-32767
	for i in range(1, n+1):
		q=max(q, p[i]+memoized_cut_rod_aux(p, n-i, r))
	r[n]=q
	return q

for j in range(31):
	print(memoized_cut_rod(p, j))





