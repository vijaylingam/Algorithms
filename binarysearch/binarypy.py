

def binarysearch(A[], n, x):
	out = False;
	if(n == 1):
		if(A[0] == x):
			return True;
		else:
			return False;

	else:
		middle = n+1/2;
		if(A[middle] == x):
			out = True;	
		else:
			if(x < A[middle]):
				B = A[:middle];
				out = binarysearch(B,middle,x);
			if(x > A[middle]):
				B = A[middle:]
				out = binarysearch(B,middle,x);			
	return out;
	
				