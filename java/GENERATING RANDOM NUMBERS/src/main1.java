import javax.swing.*;
import java.awt.*;
import java.applet.*;
public class main1 extends Frame{
    main1() {
        Frame f = new Frame("welcome");

        f.setSize(200, 300);
        f.setLocationRelativeTo(null);
//        f.setLocation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
        f.pack();
    }

    public static void main(String[] args) {
        main1 m = new main1();
    }
}
