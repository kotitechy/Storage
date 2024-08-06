import java.util.Scanner;

class p_8_if_else{
public static void main(String [] args){
Scanner sc = new Scanner(System.in);

System.out.println("Enter your Age : " );
int age = sc.nextInt();

if	(age <=18){   //if block 
System.out.println("You can't Vote, As you are Under Age");
}
else{  //else block
System.out.println("You can Vote ");
}
}
}
/*
About if-else
if-else is also an contitional Statement which makes the decision for flow of control in if there is no alternate block code to be executed when if is false the modified if statement is if-else
*/