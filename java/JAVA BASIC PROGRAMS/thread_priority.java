class myThr1 extends Thread{
    public myThr1(String name){ //---> This method will give the name of the Thread
//    super(name);  ----> If not used compiler will give name as Thread-0,1,2,3...
        super(name);
    }
    public void run(){
        int i=34;

        while(true){
            System.out.println("I am Thread ");
            System.out.println("Thank you " + this.getName());
        }
    }
}


public class thread_priority {
    public static void main(String[] args) {
        //Ready Queue: t1,t2,t3,t4,t5
        myThr1 t11 = new myThr1("Thread 1");
        myThr1 t21 = new myThr1("Thread 2");
        myThr1 t31 = new myThr1("Thread 3");
        myThr1 t41 = new myThr1("Thread 4");
        myThr1 t51 = new myThr1("Thread 5(Most important)");
        t51.setPriority(Thread.MAX_PRIORITY);
        t31.setPriority(Thread.MIN_PRIORITY);
        t41.setPriority(Thread.MIN_PRIORITY);
        t11.start();
        t21.start();
        t31.start();
        t41.start();
        t51.start();
    }
}
/*OR
multithreading environment in which thread scheduler assigns the processor to a thread based on the priority of thread. Whenever we create a thread in Java, it always has some priority assigned to it. Priority can either be given by JVM while creating the thread or it can be given by the programmer explicitly. 

Priorities in threads is a concept where each thread is having a priority which in layman’s language one can say every object is having priority here which is represented by numbers ranging from 1 to 10. 

    The default priority is set to 5 as excepted.
    Minimum priority is set to 1.
    Maximum priority is set to 10.

Here 3 constants are defined in it namely as follows:

   1. public static int NORM_PRIORITY
   2. public static int MIN_PRIORITY
   3. public static int MAX_PRIORITY

 */
