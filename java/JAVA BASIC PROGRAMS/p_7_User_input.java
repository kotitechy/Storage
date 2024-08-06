import java.util.Scanner;
class p_7_User_input {
public static void main(String args[]){
Scanner sc = new Scanner(System.in);
System.out.println("Enter Your Age : ");
int age = sc.nextInt();
if(age <= 18){
System.out.println("You Under Age So, You can't vote");
}
}
}
/*
About if Statement 
// If is an conditional Statement which acts like an logic it checks the condition if condition is true it will execute 
*/