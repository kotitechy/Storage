public class callbyvalue{
    int data = 10;
    void sum(int data){
        data+=data;
    }
    public static void main(String[] args) {
        callbyvalue c1  = new callbyvalue();
        System.out.println("Before Call sum method: "+c1.data);
        c1.sum(10);
        System.out.println("After Call sum method: "+c1.data);
    }
}