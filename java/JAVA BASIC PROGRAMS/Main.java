import java.util.Scanner;
//class
class hello {
String name;
}
// main class
public class Main {
    static int add(int a, int b)
    {
        return a+b;
    }
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a num : ");
        int a = sc.nextInt();
        System.out.println("enter a num 2 : ");
        int b = sc.nextInt();
        System.out.println(" the num is : "+ a);
        System.out.println(" the num2 is : "+ b);
        hello h1=new hello();
        h1.name="happy";
        System.out.println("ramesh21 is " + h1.name);

        System.out.println(add(a,b));
    }
}
