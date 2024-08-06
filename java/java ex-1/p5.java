import java.util.Scanner;
class p5{
    
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
System.out.println("enter a num : ");
int n = sc.nextInt();
System.out.println("The num is " + n );
int r;
for(int i = 1 ;i< 11;i++){
    r = n * i;
    System.out.println(n + " x " + i + " = " + r);
}
    }
}