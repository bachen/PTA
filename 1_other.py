import math
def printHourGlass(num,sym):
	N=int(math.sqrt(float(num+1)/2))
	p,i,t=N,0,0
	while N:
		line=(2*N-1)*sym
            	t+=2*N-1
		s=i*" "
		print "%s%s"%(s,line)
		N-=1
		i+=1
	if i>1:
		N+=2
		i-=2
		while N<=p:
			line=(2*N-1)*sym
            		t+=2*N-1
			s=i*" "
			print "%s%s"%(s,line)
			N+=1
			i-=1
	print num-t

input='1 *'
ls=input.split(" ")
num=int(ls[0])
sym=ls[1]
printHourGlass(num,sym)

		


		
