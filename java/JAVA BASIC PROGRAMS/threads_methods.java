class mythr21 extends Thread{
    public mythr21(){

    }
    public void run(){
        int i=34;

        while(true){
//            System.out.println("I am Thread ");
            System.out.println("Thank you " + this.getName());
        }
    }
}
public class threads_methods {
    public static void main(String[] args) {
        mythr21 t1 = new mythr21();
        mythr21 t2 = new mythr21();
        t1.start();
        try{
            t1.join();
        }
        catch(Exception e){
            System.out.println(e);
        }

        t2.start();

    }
}
