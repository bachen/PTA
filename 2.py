'''
def isPrime(n):
	if n == 1:
		return False
	if n < 4:
		return True
	if n % 2 == 0:
		return False
	i = 2
	while (n >= i*i):
		if n % i == 0:
			return False
		i += 1
	return True

if __name__ == '__main__':
	n = 100000 #input()
	count = 0
	i = 3
	j = 2
	while(n >= (i+j)):
		if isPrime(i+j):
			if j == 2:
				count += 1
			i=i+j
			j = 2
		else:
			j += 2
	print count'''

#coding:utf-8       
def primeRange(n):
    myArray=[1 for x in range(n+1)]  
    myArray[0]=0
    myArray[1]=0
    startPos=2
    while startPos <= n:
        if myArray[startPos]==1:
            key=2
            resultPos = startPos*key  
            while resultPos <= n:
                myArray[resultPos] =0
                key += 1
                resultPos = startPos*key
        startPos += 1

    resultList=[]  
    startPos=0
    count = 0 
    while startPos <= n-2:
        if myArray[startPos] == 1:
            if myArray[startPos + 2]==1:
            	count +=1
        startPos += 1
    return count

if __name__ == '__main__':
	n = input()
	print primeRange(n)
