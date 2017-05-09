#Author: Vijay Lingam
from __future__ import print_function
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

extra = [];
extra1 = [];
if(len(A_string)>len(B_string)):
	for i in range(0,(len(A_string)-len(B_string))):
		extra.append(0);
B = extra + B;	
if(len(B_string)-(len(A_string))):
	for j in range(0,(len(B_string)-len(A_string))):
		extra1.append(0);		
A = extra1 + A;

Product = [0]*((len(A)+len(B)));
def binaryMultiplication(a,b):
	a.reverse()
	b.reverse()
	for i in range(0,len(b)):
		carry = 0;
		for j in range(0, len(a)):
			Product[i+j] += carry + a[j] * b[i];
			carry = int(Product[i + j]/ 2);
			Product[i + j] = int(Product[i + j])%2;
		Product[i + (len(a))] += carry;
	Product.reverse()


	for i in range(0,len(Product)):
		Product[i] = str(Product[i]);
	out = ' '.join((Product))
	out = out.lstrip("0");
	print(out)
	text_file = open("output.txt", "w")
	text_file.write("%s" % out)
	text_file.close()


binaryMultiplication(A,B);

endTime = current_milli_time();
print("Total time to execute: "+ str(endTime-beginTime) + " milliseconds");	