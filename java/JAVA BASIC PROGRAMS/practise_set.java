class p_t1 extends Thread{
    @Override
    public void run() {
        int i=1;
        while(i<10){
//            if(i==9){
//          notify();
//            }
            System.out.println("Good Morning" + i);
            i++;
        }
        System.out.println(getState());
    }
}
class p_t2 extends Thread{
    @Override
    public void run() {
        int i =1;

        while(i<10){
//            try {
////              wait();
//                sleep(12);
//
//
//            } catch (InterruptedException e) {
//                throw new RuntimeException(e);
//            }
            System.out.println("Welcome1");
            i++;
        }
    }
}
public class practise_set {
    public static void main(String[] args) {
        p_t1 t1 = new p_t1();
        p_t2 t21 = new p_t2();
        t1.getPriority();
        System.out.println(t1.getPriority());
        System.out.println(t1.getName());
        System.out.println(t1.getClass());
        System.out.println(t1.getState());
//        System.out.println(t1.isAlive());
        t1.start();
        System.out.println(t1.getState());
        System.out.println(Thread.currentThread().getState());
        System.out.println(t1.toString());
        t21.start();
    }
}


