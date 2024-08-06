import java.applet.*;  
import java.awt.*;  
public class app extends Applet  
{  
    Image pic;  
    public void init()  
    {  
        pic = getImage(getDocumentBase(), "images.jpeg");  
    }  
    public void paint(Graphics grp)  
    {  
        grp.drawImage(pic, 100, 30, this);  
    }  
}  
/* 
<applet code="app.class" width="400" height="400"> 
</applet>
*/