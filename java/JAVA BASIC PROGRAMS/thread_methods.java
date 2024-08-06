
import java.lang.*;
class thread1 extends Thread{
    int i=10;
thread1(){         //default constructor
    System.out.println("Constructor called");
}
    @Override
    public void run() {
        while(i<30){
            try {
                sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
            System.out.println("A i: " + i);
            i++;
        }
    }


}
class thread2 extends Thread implements Runnable{
    thread2(String name){
        this.setName(name);
        System.out.println("Name setted ");

    }
    thread2(){
        String na = this.getName();
        System.out.println("Getter called name: "+ na);
    }
    int j = 50;

    @Override
    public void run() {
        while (j < 70) {
                System.out.println("B J: " + j);
            j++;
        }
    }

}
public class thread_methods {
    public static void main(String[] args) {
        thread1 b1 = new thread1();
        thread2 b2 = new thread2();
        Thread g2 = new Thread(b2, "Shiva");
//        b1.setPriority(Thread.MIN_PRIORITY);
        b1.setPriority(1);
        int a = b2.getPriority();
        int b = b1.getPriority();
        System.out.println("Priority : " + a);
        System.out.println("Priority : " + b);
        b1.start();
        b2.setDaemon(true);
        b2.start();
    }
}
