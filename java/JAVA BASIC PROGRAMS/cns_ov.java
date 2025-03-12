public class cns_ov {
    
    public static void main(String[] args) {
        Adds a1 =new Adds(10, 20);
        Adds a2 =new Adds(10.2f, 20.2f,3.1f,1.1f);
        Adds a3 =new Adds(10.32525, 20.32325,4.23524);
        Adds a4 =new Adds(10, 20);
        
    }
}
class Adds {
    Adds(int a,int b){
        System.out.println("Sum of "+a+","+b+":"+(a+b));
    }
    Adds(float a,float b,float c,float d){
        System.out.println("Sum of "+a+","+b+","+c+","+d+":"+(a+b+c+d));
    }
    Adds(double a,double b, double c){
        System.out.println("Sum of "+a+","+b+","+c+":"+(a+b+c));
    }
    
}