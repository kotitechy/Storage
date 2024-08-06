package java_programs1.src;

class Room{
    float length;
    float breadth;
    void getdata(float a,float b){
        length = a;
        breadth = b;
    }
}
public class constructors {

    public static void main(String[] args) {
        float area;
        Room room1 = new Room();  //creates an object room1
        room1.getdata(10.0f,20.0f);  //Assigning he values to len and bre
        area = (room1.length * room1.breadth);
        System.out.println("The area is: " + area);
    }
}
