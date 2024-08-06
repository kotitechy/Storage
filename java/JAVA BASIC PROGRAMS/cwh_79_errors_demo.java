import java.util.Scanner;

public class cwh_79_errors_demo {
    public static void main(String[] args) {
        //write a program to print all logical errors
        //logical error is the Thoughest error
        for(int i=0;i<11;i++){
            if(i%2==1){
                System.out.println(i);
                //1
                //3
                //5
                //7
                //9  here all are prime but 9 is not a prime so, it is a logical error
            }
        }
        //run time errors
        //if we want to add 2 numbers but if we give the string values it crashes this is a run runtime error an ide/compiler also don't know how to handle it
        //ex:-
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int a1 = sc.nextInt();
        System.out.println("Enter another number : ");
        int a2 = sc.nextInt();
        System.out.println("The sum is : " + (a1+a2));
    }
}
