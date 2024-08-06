//fonts in java
import java.applet.*;
import java.awt.*;

class setfont extends Applet{
    Font obj = new Font("Times New Roman ",Font.ITALIC,100);
    public void paint(Graphics g){
g.setFont(obj);
        g.drawString("Jai Ganesha..",10,20);

    }
}
//<applet code="applet_6.class" width=100 height=100></applet>