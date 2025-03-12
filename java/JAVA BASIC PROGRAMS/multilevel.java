class square{
    int l;
    void area(){
        System.out.println("Area of Square : "+(l*l));
    }
}
class rect extends square{
    int b;

    void perimeter(){
        System.out.println("Perimeter of rectangle: "+(2*(l+b)));
    }
}
class cubiod extends rect{
    int h;
    void volume(){
        System.out.println("Volume od Cubiod : "+(l*b*h));
    }
}       
public class multilevel {
    public static void main(String[] args) {
        cubiod c1 = new cubiod();
        c1.l=10;
        c1.b=10;
        c1.h=10;
        c1.area();
        c1.perimeter();
        c1.volume();
    }
}
