import java.util.Scanner;

public class Big3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        if ((a > b) && (a > c)) {
            System.out.println("A is big");
        }
        if (b > a && b > c) {
            System.out.println("B is Big");
        }
        if (c > a && c > b) {
            System.out.println("c is Big");
        } else {
            System.out.println("None is Big");

        }
        sc.close();
    }
}
