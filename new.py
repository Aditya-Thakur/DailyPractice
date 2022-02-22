#Python3 program to count total number of
#special sequences of length n where
#Recursive function to find the number of
# special sequences

def getTNH(m,n):
	if m<n:
		return 0
	if n==0:
		return 1
	res=(getTNH(m-1,n)+
		getTNH(m//2,n-1))
	return res
m,n = raw_input().split()
print(getTNH(int(m),int(n)))
