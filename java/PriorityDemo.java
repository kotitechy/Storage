import java.util.Scanner;

class PriorityDemo extends Thread {
    public void run() {
    	System.out.print("Thread name: "+Thread.currentThread().getName()+ ", Priority: " +Thread.currentThread().getPriority()+"\n");
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        PriorityDemo thread1 = new PriorityDemo();
        PriorityDemo thread2 = new PriorityDemo();

        System.out.println("Enter priority for Thread 1 (minimum/maximum):");
        String priorityInput1 = scanner.nextLine().toLowerCase();
        System.out.println("Enter priority for Thread 2 (minimum/maximum):");
        String priorityInput2 = scanner.nextLine().toLowerCase();

        int priority1 = getPriorityValue(priorityInput1);
        int priority2 = getPriorityValue(priorityInput2);

        thread1.setPriority(priority1);
        thread2.setPriority(priority2);

        thread1.start();
        thread2.start();

        scanner.close();
    }

    private static int getPriorityValue(String input) {
        if (input.equals("minimum")) {
            return Thread.MIN_PRIORITY;
        } else if (input.equals("maximum")) {
            return Thread.MAX_PRIORITY;
        } else {
            System.out.println("Invalid input. Setting priority to default.");
            return Thread.NORM_PRIORITY;
        }
    }
}

