def rotate(nums,n,k):
    length = n
    while(k > length):
        k = k - length
    res = []
    for i in xrange(-k,length-k,1):
        res.append(str(nums[i]))
    print ' '.join(res)

if __name__=='__main__':
    raw_inp1 = raw_input()
    raw_inp2 = raw_input()
    inp1 = raw_inp1.split(' ')
    n = int(inp1[0])
    k = int(inp1[1])
    inp2 = raw_inp2.split(' ')
    inp=[]
    for i in inp2:
        inp.append(int(i))
    rotate(inp,n,k)