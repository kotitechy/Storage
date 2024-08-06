class Mythread11 implements Runnable{

    @Override
    public void run() {
        System.out.println("I am an thread-1 not a threat");
        System.out.println("I am an thread-1 not a threat");
        System.out.println("I am an thread-1 not a threat");
        System.out.println("I am an thread-1 not a threat");
        System.out.println("I am an thread-1 not a threat");
        System.out.println("I am an thread-1 not a threat");
    }
}
class Mythread22 implements Runnable{

    @Override
    public void run() {
        System.out.println("I am an thread-2 not a threat");
        System.out.println("I am an thread-2 not a threat");
        System.out.println("I am an thread-2 not a threat");
        System.out.println("I am an thread-2 not a threat");
        System.out.println("I am an thread-2 not a threat");
        System.out.println("I am an thread-2 not a threat");
        System.out.println("I am an thread-2 not a threat");
    }
}
public class runnable {
    public static void main(String[] args) {
        Mythread11 bullet1 = new Mythread11();
        Thread gun2 = new Thread(bullet1);
        Mythread22 bullet2 = new Mythread22();
        Thread gun1 = new Thread(bullet2);


        gun1.start();
        gun2.start();
    }
}
