//P-SERIES WRITTEN BY KTC 
//P-5. USER INPUT 

import java.util.Scanner;

public class p5{
public static void main(String [] args){
Scanner sc = new Scanner(System.in);
System.out.println("ENTER YOUR NAME : ");
String str = sc.nextLine();  //string input

System.out.println("ENTER YOUR ROLLNO : ");
int a = sc.nextInt();  //INTEGER INPUT

System.out.println("STUDENT DETAILS: " );
System.out.println("NAME   : " + str);
System.out.println("ROLLNO : " + a);
 

}
}