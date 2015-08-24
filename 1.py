'''

def build(n):
	if n == 1:
		print '*'
		return
	count = 0
	left = n-1
	mark = 3
	while(left >= 2*mark):
		left -= 2*mark
		mark += 2
		count += 1
	limit = mark-2
	for i in xrange(count+1):
		print ' '*i+'*'*limit+' '*i
		limit -= 2
	limit += 2
	for i in xrange(count-1,-1,-1):
		limit += 2
		print ' '*i+'*'*limit+' '*i
	if left != 0:
		print left
	return'''

raw_inp = '1 *'#raw_input() # '19 .'
inp = raw_inp.split(' ')
n = int(inp[0])
s = inp[1]

count = 0
left = n-1
mark = 3
while(left >= 2*mark):
	left -= 2*mark
	mark += 2
	count += 1
limit = mark-2
for i in xrange(count+1):
	print ' '*i+s*limit
	limit -= 2
limit += 2
for i in xrange(count-1,-1,-1):
	limit += 2
	print ' '*i+s*limit
print left