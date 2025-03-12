import java.util.Scanner;

public class sqrs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no f elements: ");
        int n= sc.nextInt();
        int[] a=new int[n];
        System.out.println("Enter Elements oe by one: ");
        for(int i=0;i<n;i++){
            a[i]=sc.nextInt();
            a[i]*=a[i];
        }
        System.out.println("Squares : ");
        for(int i=0;i<n;i++){
            System.out.print(a[i]+"->");
        }
    }
}
