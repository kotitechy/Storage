class myThr extends Thread{
    public myThr(String name){ //---> This method will give the name of the Thread
//    super(name);  ----> If not used compiler will give name as Thread-0,1,2,3...
super(name);
    }
    public void run(){
        int i=34;
        System.out.println("THank you");
//        while(true){
            System.out.println("Iam Thread");
//        }
    }
}

public class threadclassconstructors {
    public static void main(String[] args) {
    myThr t1 = new myThr("Shiva");
    myThr t2 = new myThr("Charan");
    t1.start();
    t2.start();
        System.out.println("The id of the Thread is: " + t1.getId());
        System.out.println("The name of the Thread is: " + t1.getName());
        System.out.println("The id of the Thread-2 is: " + t2.getId());
        System.out.println("The name of the Thread-2 is: " + t2.getName());
        System.out.println("The ");
    }
}
