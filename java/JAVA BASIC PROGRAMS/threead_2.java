class thread11 implements Runnable {
    @Override
    public void run() {
        int i=2;
        while(i>1&&i<19){
            System.out.println("i+1: " + i);
            i++;
        }
    }
}
class thread22 implements Runnable{
    @Override
    public void run() {
        int i=222;
        while(i>221&&i<239){
            System.out.println("j: " + i);
            i++;
        }
    }
}
public class threead_2 {
    public static void main(String[] args) {
        thread11 bullet1 = new thread11();
        Thread gun1 = new Thread(bullet1);   //new state
        thread22 bullet2 = new thread22();
        Thread gun2 = new Thread(bullet2);
        gun1.start();   //----> AfterThread is in new the Thread Scheduler makes it Runnable -->Ready to Launch
        gun2.start();
    }
//Thread Running
    //Non-Runnable State ----> In this state the Thread Scheduler makes the threads stop which are waiting for input
}
