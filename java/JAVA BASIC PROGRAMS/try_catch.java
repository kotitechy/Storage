import java.util.Scanner;
public class try_catch {
    public static void main(String[] args) {
/*
types of exceptions in java are
1. Null pointer exception
2. Arithmetic exception
3. Array index out of bonds  exception
4. Illegal argument exception
5. Number format exception
 */
//        2. Arithmetic exception
       try{
           int a = 6000;
           int b  = 9;
           int c = a/b;
           System.out.println("The division of a,b is" + c);
           System.out.println("process completed Successfully");
       }
       catch (Exception a){
           System.out.println("we failed to divide : Reason : ");
           System.out.println(a);
       }

    }
}