//Switch Statement 
import java.util.Scanner;
class p_10_Switch_Statement{
public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
	System.out.println(" Java is \n 1. pure object oriented \t 2. procedure oriented \n 3. object oriented \n 4. none ");
	System.out.println("Enter your choice : ");
	int ch = sc.nextInt();
	switch(ch){
	case 1:
	System.out.println("Correct answer");
	System.out.println("Correct answer is : Pure object oriented ");
	break;
	
	case 2:
	System.out.println("In-Correct answer");
	System.out.println("Correct answer is : Pure object oriented ");
	break;
	
	case 3:
	System.out.println("In-Correct answer");
	System.out.println("Correct answer is : Pure object oriented ");
	break;
	
	case 4:
	System.out.println("In-Correct answer");
	System.out.println("Correct answer is : Pure object oriented ");
	break;
	
	default :
	System.out.println("In valid choice");
	break;
	}
}
}
/*
In computer programming languages, a switch statement is a type of selection control mechanism used to allow the value of a variable or expression to change the control flow of program execution via search and map.
*/