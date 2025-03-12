final class animal{
    final void task(){
        System.out.println("Sleeping....");
    }
}
// class dog extends animal{
    // @Override
    // void task(){
    //     System.out.println("Barking.....");
    // }
// }
public class finals {
    public static void main(String[] args) {
        final double pi = 22/7;
        // pi=3.14; --> not possible
        System.out.println("Pi : "+pi); 
        animal a1 = new animal();
        a1.task();       
    }
}
