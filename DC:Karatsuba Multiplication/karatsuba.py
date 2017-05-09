from __future__ import print_function
import math;
import time
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


Sum1 = [0]*(len(A));

def add(lhs, rhs):
    length = max(len(lhs), len(rhs))
    lhs = [0 for i in range(len(lhs), length)] + lhs;
    rhs = [0 for i in range(len(rhs), length)] + rhs;

    carry = 0

    result = [];

    for i in range(1, len(lhs) + 1):
        column = lhs[-i] + rhs[-i] + carry;
        result.append(column % 2);
        carry = column / 2;

    if carry != 0: result.append(carry)
    result.reverse();

    return result;
	

def karatsuba(A,B):
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
	if((len(A) == 1)&(len(B) == 1)):
		return(A[0]*B[0]);
	else:
		A_left = A[0:mid];
		A_right = A[mid:len(A)];
		B_left = B[0:mid];
		B_right = B[mid:len(B)];

		P = karatsuba(A_left,B_left);
		Q = karatsuba(A_right,B_right);
		R = karatsuba(add(A_left,A_right), add(B_left, B_right))-P-Q;

		return(((2**(2*int(math.ceil(len(A)/2))))*P) + ((2**(1*int(math.ceil(len(A)/2)))*(R))) + Q);

y =(karatsuba(A,B));
#print(y);
out = str(bin(y));	
out = out[2:];
out = out.lstrip("0");
text_file = open("output.txt", "w")
text_file.write("%s" % out)
text_file.close()
endTime = current_milli_time();
print("Total time to execute: "+ str(endTime-beginTime) + " milliseconds");	