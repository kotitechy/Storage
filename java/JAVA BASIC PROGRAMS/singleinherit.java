class rect{
    int l,b;

    void area(){
        System.out.println("Area of rectangle: "+(l*b));
    }
}
class cubiod extends rect{
    int h;
    void volume(){
        System.out.println("Volume od Cubiod : "+(l*b*h));
    }
}
public class singleinherit {
    public static void main(String[] args) {
        cubiod c1  = new cubiod();
        c1.l=10;
        c1.b=10;
        c1.h=10;
        c1.area();
        c1.volume();
    }
}
