import java.io.*;
import java.lang.Integer;
import java.util.*;

public class BS {


    public static boolean binarySearch(int[] A, int n, int x) {
        boolean out = false;
        //System.out.println("Looking for: "+x);
        if (n == 1) {
            if (A[0] == x) {
                return true;
            } else {
                return false;
            }
        } else {
            int middle;
            middle = n + 1/ 2;
            //System.out.println("middle element: " + A[middle]);


            if (A[middle] == x) {
                //System.out.println(x + " exists");
                out = true;
            } else {
                if (x < A[middle]) {

                    int[] B = new int[middle];
                    System.arraycopy(A, 0, B, 0, middle);

                    out = binarySearch(B, middle, x);

                } if(x > A[middle]) {
                    int[] B = new int[middle];
                    System.arraycopy(A, middle, B, 0, (n - middle));

                    out = binarySearch(B, middle, x);

                }

               // System.out.println(out);

            }

        }
    return out;
    }


     
    
    
    public static void main(String args[]) {
        
        
        int n=0;//This is the size of the array
        int x=0;//This is the number that is supposed to be searched in the array
        int A[] = new int[0];//This is the array with default initialization
        
        //The input is read from a file named "input.txt".
        //The first line contains the size of the integer array.
        //The second line of this file contains the integers (comma separated) of the array.
        //The third line contains the integer to be searched.
        try {
            BufferedReader BR = new BufferedReader(new FileReader("input.txt"));
            String line = BR.readLine();
            n = Integer.parseInt(line);
            
            //Initialize array A
            A = new int[n];
            
            //Read the second line of the file and initialize the array A
            line = BR.readLine();
            String[] dataArray = line.split(",");
            for(int i=0;i<n;++i){
                A[i] = Integer.parseInt(dataArray[i]);
            }
            
            //Read the third line of the input file
            line = BR.readLine();
            x = Integer.parseInt(line);
            
            //Close the file
            BR.close();
            
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    
        
        if(binarySearch(A, n, x))System.out.println("Yes");
        else System.out.println("No");
        
    }
}