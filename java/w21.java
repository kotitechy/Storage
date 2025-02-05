public class w21 {
    static int a,b;
    public static void main(String[] args) {
        if(args.length<=0){
            System.out.println("Enter Command line args.");
        }else{
            w21.a=Integer.parseInt(args[0]);
            w21.b=Integer.parseInt(args[1]);
            w21.total();
        }
        System.out.println("Program completed.");
    }
    public static void total(){
        int tot=a+b;
        int avg=(a+b)/2;
        System.out.println("total: "+tot);
        System.out.println("Average: "+avg);
    }
}
