public class thread {
    public static  int func(){
        return 10/0;
    }
    public static void main(String[] args) {
        try{
            System.out.println(func());
        }
        catch (Exception e){
            System.out.println("This is an Exception");
        }
        finally {
            System.out.println("End of program");
        }
    }
}
