class shape{
    int len;
    int bre;
    float rad;
    shape(int x,int y){
    System.out.print("The area of rectangle:  " + (x * y));
    }
    shape(int r){
    r=radius;
    System.out.println("The area of circle is: " + (2 * 3.14 * rad));
    }

}

class fun_over_load{
    public static void main(String args[]){
    shape rec1 = new shape(10,20);
    shape cir1 = new shape(1);
    
}
}