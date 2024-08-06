package java_programs1.src;

class Super{
    int x;
    Super(){
        this.x = x= 10;
    }
    void dsiplay(){
        System.out.println("Super x = " + x);
    }
        }
        class Sub extends Super{
    int y = 20;
    Sub(){
        this.y = y;
    }
    void display(){
        System.out.println("Super x = " + x);
        System.out.println("Sub y = " + y);
    }
        }
public class over_ride {
    public static void main(String[] args) {
        Sub s1 = new Sub();
        s1.display();
    }
}
