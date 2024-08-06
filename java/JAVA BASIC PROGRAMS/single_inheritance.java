package java_programs1.src;

import java.util.Scanner;

class student {
    Scanner sc = new Scanner(System.in);
    int rno;
    String name;
    float marks;

    student() {
        System.out.println("Getting data");
        System.out.println("Enter the student name");
        name = sc.nextLine();
        System.out.println("enter student rollno: ");
        rno = sc.nextInt();
        System.out.println("Enter student marks: ");
        marks = sc.nextFloat();
    }

    void putdata() {
        System.out.println("Putting data");
        System.out.println(" Student Roll no: " + rno + "\n Name: " + name + "\n marks: " + marks);
    }
}

public class single_inheritance {
    public static void main(String[] args) {
        student s1 = new student();
        s1.putdata();

    }
}
