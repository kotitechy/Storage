class Mythread extends Thread{
    @Override
    public void run() {
        int i=2;
while (true){

    System.out.println(i);
}
    }
}
class MYthread2 extends Thread{
    int i=2;
    @Override
    public void run() {
        while(true){
            i=3;
            System.out.println(i);
        }
    }
}
public class threads {
    public static void main(String[] args) {
        Mythread t1 = new Mythread();
        MYthread2 t2 = new MYthread2();
        t1.start();
        t2.start();
    }
}
