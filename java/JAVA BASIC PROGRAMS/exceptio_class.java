import java.util.Scanner;
import java.util.Scanner.*;
class MyException extends Exception{
    @Override
    public java.lang.String toString() {
        return super.toString() + "This is shiva";
    }

    @Override
    public java.lang.String getMessage() {
        return super.getMessage() + "  I am Shiva-1";
    }
}

class age extends Exception{
    @Override
    public java.lang.String toString() {
        return super.toString() + "Age will not be 112";
    }

    @Override
    public java.lang.String getMessage() {
        return super.getMessage() + "  Make sure age is valid";
    }
}

public class exceptio_class extends Exception{

    public static void main(String[] args) throws MyException, age {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
//int a=9;
if(a<9) {
    try {
//        throw new ArithmeticException("Number < 9");
        throw new MyException();
    }
    catch (Exception e){
        System.out.println(e.getMessage());
        System.out.println(e.toString());
        e.printStackTrace();
        System.out.println("Finished");
    }
}
if(1==1){
    throw new ArithmeticException("Hello");
}


        System.out.println("YES Finished");

/*
Exceptions 2types:
1. built in
2. customized exceptions
check oracle documentation for more
 */
    }
}
