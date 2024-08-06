//P-SERIES WRITTEN BY KTC 
//p-8. EVEN/ODD NUMBER
import java.util.Scanner;
public class p8 {
    public static void main(String[] args) {
        System.out.println("ENTER A NUMBER : ");
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        if(a%2==0){
            System.out.println("THE NUMBER IS EVEN ");
        }
        else{
            System.out.println("THE NUMBER IS ODD");
        }
    }
}
