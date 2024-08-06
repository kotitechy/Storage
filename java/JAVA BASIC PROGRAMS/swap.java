package java_programs1.src;

public class swap {
    void swap(int x, int y){
        System.out.println("Before swap: \n x = " + x + " y = " + y);
        int temp = x;
        x = y;
        y = temp;
        System.out.println("Before swap: \n x = " + x + " y = " + y);
    }
    public void main(String[] args) {

       swap(10 ,20);
    }
}
