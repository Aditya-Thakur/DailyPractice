package q1;

import java.util.Scanner;

public class Tester {

    static int  getTotalNumberOfSequences(int m, int n)
    {
        // A special sequence cannot exist if length
        // n is more than the maximum value m.
        if(m < n)
            return 0;
      
        // If n is 0, found an empty special sequence
        if(n == 0)
            return 1;
      
        // There can be two possibilities : (1) Reduce
        // last element value (2) Consider last element
        // as m and reduce number of terms
        return getTotalNumberOfSequences (m-1, n) +
               getTotalNumberOfSequences (m/2, n-1);
    }  
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        scanner.close();
        System.out.println(getTotalNumberOfSequences(m, n));

    }
}
