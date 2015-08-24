
def doubled(n):
	length = len(n)
	long_flag = False
	end = -1
	if length > 32:
		long_flag = True
		end = length - 33
	mov = 0
	res = []
	for i in xrange(length-1,end,-1):
		tmp = int(n[i])+int(n[i])+mov
		if tmp < 10:
			res.append(str(tmp))
			mov = 0
		else:
			res.append(str(tmp%10))
			mov = 1
	if mov == 1:
		res.append(str(mov))
	res = res[::-1]
	str_res= ''.join(res)

	flag = True
	for i in range(1,10):
		if str(i) not in str_res:
			flag = False
	if (flag == True) & (long_flag == False):
		print 'Yes'
	else:
		print 'No'
	return int(str_res)

if __name__ == '__main__':
	n = str(123456789999123456789999123456789999)#raw_input()
	print doubled(n)