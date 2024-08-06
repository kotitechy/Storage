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
                frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
                frame.setTitle("SHIVA'S");
                frame.setResizable(false);
                frame.setVisible(true);
                frame.setLocation(1000,30);
                frame.setBackground(new Color(1.0f,1.0f,1.0f,0.5f));
//                frame.setAlwaysOnTop(true);-->sets it's self on top when other apps opened

                //time
                l1 = new JLabel();
                frame.add(l1);
                l1.setFont(f1);
                for (int i =1; i > 0 ; i++) {
                    Date d = new Date();
                    SimpleDateFormat f = new SimpleDateFormat("hh:mm:ss aa");
                    String time = f.format(d);
                    l1.setText(time);
                }

//
            }
        }