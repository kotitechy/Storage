package java_programs1.src;
import java.util.Scanner;

final class student_class{
    //by using final class we can't create more-classes of a base-class
    Scanner sc= new Scanner(System.in);
    final int rollno = 18; //by using final we can't re-assign the value to a variable
    String name;
    final void getdata(){
        System.out.println("Enter student Name: ");
        name = sc.nextLine();
    }
    void putdata(){
        System.out.println("Student details: \n Name: " + name + "\n Roll-no: " + rollno);
    }

}
//    class result extends student_class{result =111; // is illegal}  can't be used or accesed
 class finalisers {
    public static void main(){
        student_class s1 = new student_class();
        System.out.println("Hello world");
        s1.getdata();
        s1.putdata();

    }
}
