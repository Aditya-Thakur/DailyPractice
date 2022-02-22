package q1;
import java.util.*;

class New{
    
static int sumDivisibles(int A, int B)
{
	int sum = 0;
	for (int i = A; i <= B; i++)
		if (i % 7 == 0)
			sum += i;
	return sum;
}

// Driver code
public static void main(String[] args)
{
	int A = 1, B = 20, M = 7;
	System.out.print(sumDivisibles(A, B) +"\n");
}
}

// This code is contributed by 29AjayKumar
