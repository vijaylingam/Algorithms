from __future__ import print_function
import math;
import time;
current_milli_time = lambda: int(round(time.time() * 1000))

beginTime = current_milli_time();

A = [];
B = [];

Product = [];
file = open('input.txt', 'r')
A_string = str(file.readlines()[0])
file = open('input.txt', 'r')
B_string = str(file.readlines()[1])

for i in range(0,len(A_string)-1):
	A.append(int(A_string[i]));
for i in range(0,len(B_string)-1):
	B.append(int(B_string[i]));	

def DCMultiply(A,B):
	extra = [];
	extra1 = [];
	if(len(A)>len(B)):
		for i in range(0,(len(A)-len(B))):
			extra.append(0);
	B = extra + B;	
	if(len(B)-(len(A))):
		for j in range(0,(len(B)-len(A))):
			extra1.append(0);		
	A = extra1 + A;

	mid = (len(A)+1)/2;
	if((len(A) == 1)|(len(B) == 1)):
		return(A[0]*B[0]);
	else:
		P = DCMultiply(A[:mid],B[:mid]);
		Q = DCMultiply(A[:mid],B[mid:len(B)]);
		R = DCMultiply(A[mid:len(A)],B[:mid]);
		S = DCMultiply(A[mid:len(A)],B[mid:len(A)]);
		return(((2**(2*int(math.ceil(len(A)/2))))*P) + ((2**(1*int(math.ceil(len(A)/2)))*(Q+R))) + S);


out = str(bin(DCMultiply(A,B)));
out = out[2:];
out = out.lstrip("0");
text_file = open("output.txt", "w")
text_file.write("%s" % out)
text_file.close()
endTime = current_milli_time();
print("Total time to execute: "+ str(endTime-beginTime) + " milliseconds");	
