public class passbyref {
    int data = 10;
    void sum(passbyref ob){
        ob.data+=ob.data;
    }
    public static void main(String[] args) {
        passbyref c1  = new passbyref();
        System.out.println("Before Call sum method: "+c1.data);
        c1.sum(c1);
        System.out.println("After Call sum method: "+c1.data);
    }
}
