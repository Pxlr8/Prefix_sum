import java.util.Scanner;

public class PrefixSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = sc.nextInt();
        int[] arr = new int[n + 1]; 
        int[] prefix = new int[n + 1];

        System.out.println("Enter array elements:");
        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
            prefix[i] = prefix[i - 1] + arr[i]; 
        }

        System.out.print("Enter number of queries: ");
        int q = sc.nextInt();

        System.out.println("Enter queries (L R):");
        while (q-- > 0) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            System.out.println("Sum: " + (prefix[r] - prefix[l - 1]));
        }

        sc.close();
    }
}