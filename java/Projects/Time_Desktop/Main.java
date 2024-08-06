import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Main {

    static   Font f1 =new Font("Dialog",Font.BOLD,35);

            static Font f2 =new Font("Forte",Font.PLAIN,24);

    static  Font f3 =new Font("Elephant",Font.ITALIC,35);
            static JLabel l1;
            public static void main(String[] args) {
                JFrame frame = new JFrame();
                frame.setSize(200, 30);
                frame.setUndecorated(true);
                frame.setResizable(false);
                frame.setVisible(true);
                frame.setLocation(1050,20);
                //time
                l1 = new JLabel();
                frame.add(l1);
                l1.setFont(f1);
                while(true){
                    Date d = new Date();
                    SimpleDateFormat f = new SimpleDateFormat("hh:mm:ss aa");
                    String time = f.format(d);
                    l1.setText(time);
                }
            }
        }