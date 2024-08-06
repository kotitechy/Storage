import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class main1 extends Applet implements ActionListener{
    public static void func(){
       System.out.println("Hello");
    }
    public static void main(String []args){
        System.out.println("Hello");
        func();
    }
}