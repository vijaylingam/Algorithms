#Author: Vijay Lingam

from __future__ import print_function
import time;
current_milli_time = lambda: int(round(time.time() * 1000))

beginTime = current_milli_time();

A = [];
B = [];
Sum = [];
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
Sum = [0]*(len(A)+1);

def binaryAddition(a,b):
	carry = 0;
	for index in range((len(a)-1),-1, -1):
		tempSum = a[index] + b[index] + carry;
		if(tempSum == 1):
			carry = 0;
			Sum[index+1] = 1;

		if(tempSum == 0):
			carry = 0;
			Sum[index+1] = 0;

		if(tempSum==2):
			Sum[index+1] = 0;
			carry = 1;

		if(tempSum == 3):
			Sum[index+1] = 1;
			carry = 1;
	if(carry):
		Sum[0] = 1;	

	for i in range(0,len(Sum)):
		Sum[i] = str(Sum[i]);				
	out = ''.join(Sum);
	out = out.lstrip("0");
	text_file = open("output.txt", "w")
	text_file.write("%s" % out)
	text_file.close()	

binaryAddition(A,B);
endTime = current_milli_time();
print("Total time to execute: "+ str(endTime-beginTime) + " milliseconds");		
