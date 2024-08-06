package java_programs1.src;
class a{              //base-class
    int a = 111;
}
class b extends a{      //intermideate-class
    int b = 2000;
}
class c extends b{      //derived-class
    int c = 1000;
    c(){
        System.out.println("A = " + a);
        System.out.println("B = " + b);
        System.out.println("C = " + c);
    }
}
public class mutilevel_inherit {
    public static void main(String[] args) {
        c ob = new c();
    }
}
