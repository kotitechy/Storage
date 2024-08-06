import java.applet.*;
import java.awt.*;
public class app1 extends Applet {
    public void paint(Graphics grp){
    for (int i = 1; i >0; i++)  
        {  
            grp.drawRect(i, i+1, 20, 20);
            try  
            {  
                Thread.sleep(100);  
            } catch (Exception e) {}  
        } 
}
}
/*<applet code="app1.class" width="1000" height="1000"> 
</applet>
*/