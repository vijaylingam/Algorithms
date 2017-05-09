x = [1,2,2^2,2^3,2^4,2^5,2^6,2^7,2^8,2^9,2^10,2^11,2^12,2^13,2^14,2^15,2^16];
longmul = [0,0,0,0,0,1,3,8,29,122,490,1887,7580,30025,124631,493916,2172349];
DCmul = [0,0,0,1,2,5,14,43,170,666,2548,10428,41885,164629,774295,3097180,12388720];
karatsuba = [0,0,0,1,2,4,13,42,130,361,1046,3202,9250,28525,84025,298756,862761];
title('Long Multiplication vs DC Multiplication vs Karatsuba')
hold on;
xlabel('Size of n')
hold on;
ylabel('Time in milliseconds')
hold on;
plot(x,longmul);
hold on;
plot(x, DCmul, 'g');
hold on;
plot(x, karatsuba, 'r');
hold on;
legend('y = longmul','y = DCmul','y = karatsuba','Location','northwest');