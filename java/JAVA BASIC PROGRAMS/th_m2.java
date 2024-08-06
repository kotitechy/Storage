
import  java.lang.*;
import java.util.Scanner;


class t3 extends Thread{
    int s1;

     t3(String name){
        super(name);
         System.out.println("setted name is: " + name);
         System.out.println("ENter a value");
         Scanner sc = new Scanner(System.in);
         s1 = sc.nextInt();
    }
    @Override
    public void run() {
         int i=1;
        while(i<111){
            System.out.println("Thread class A : " + (i++));


        }
    }
}
class t4 extends Thread{
    t4(String name){
        super(name);
        System.out.println("setted name is: " + name);
    }
    @Override
    public void run() {
        int i=1;
        while(i<111){
            System.out.println("Thread class B : " + (i++));


        }
    }
}
public class th_m2 {
    public static void main(String[] args) {
        t3 t1 = new t3("Shiva");
        t4 t2 = new t4("Shiva-111");
        t1.start();
        try{
            t1.join();
        }
        catch (Exception e){
            System.out.println(e);
        }
//        t1.join();
        t2.start();
        int i =10;
       float j = (float) i;
        System.out.println(j);
    }
}
