//if-else ladder / nested if
import java.util.Scanner;
class p_9_if_else_ladder{
public static void main(String [] args){
System.out.println("Enter your percentage : ");
Scanner sc = new Scanner(System.in);
float p = sc.nextFloat();

if (p <=90){  //nested if
	if (p >= 75){
	System.out.println("Distinct pass");
	}
}
else if(p >= 65 || p < 75){
	System.out.println("You are top");
}


if (p >= 35 && p >= 50){
System.out.println("You are Average");	
}
else if(p >= 0 && p < 35){
System.out.println("You are failed");
}


}
}
/*
About if else ladder
it is also an conditional statement which checks muitiple if and else Statements in ladder  format
*/