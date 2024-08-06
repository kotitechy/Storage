import java.awt.*;
import java.applet.*;

public class main12 extends Applet{
    int h,w;
    public void init(){
        h = getSize().height;
        w = getSize().width;
        setName("Narayana");
    }
    public void paint(Graphics g){
        g.drawRoundRect(10,30,120,120,2,3);
    }

    public static void main(String[] args) {
    main12 m1 = new main12();
    m1.setName("Shiva");
    m1.init();
    m1.paint(m1.getGraphics());
    }
}
