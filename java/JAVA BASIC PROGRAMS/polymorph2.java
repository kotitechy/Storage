class shape{
    int l;
    final double pi=22/7;
    void area(){
        System.out.println("No area for now");
    }
}

class square extends shape{
    @Override
    void area(){
        super.area();
        System.out.println("Square Area: "+(l*l));
    }
}

class circle extends shape{
    void area(){
        System.out.println("Circle Area : "+(pi * (l*l)));
    }
}

public class polymorph2 {
    public static void main(String[] args) {
        square sq  =  new square();
        circle c1  =  new circle();
        sq.l=10;
        c1.l=10;
        
        sq.area();
        c1.area();
    }
}
