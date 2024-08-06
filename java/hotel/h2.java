import java.applet.*;
import java.awt.*;

class h2 extends Applet{
Image i1;

public void init(){
i1 = getImage(getDocumentBase(), "images.jpeg");
}
public void paint(Graphics g){
g.drawString("Hello",10,10);
g.drawImage(i1,20,20,this);

}

}
//<Applet code="h2.class" width=200 height=200></Applet>