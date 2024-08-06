class shape{
    int len;
    int bre;
    float rad;
    shape(int x,int y){
     System.out.println("The area of recatngle: " +  (x * y));
    }
    shape(int r){
    r=rad;
     System.out.println("The area of recatngle: " + (2 * 3.14 * rad));
    }

}
class square extends shape{
    int side;
    square(int s){
    super (rad);
    s = side;
    System.out.println((4 * side));
    }
    
}

class fun_over_load{
    public static void main(String args[]){
    square rec1 = new shape(10,20);
    square cir1 = new shape(1);
    square sq = new square(4);
    
}
}