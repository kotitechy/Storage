import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

class breakfast extends Applet implements ActionListener{
    
    Image wel,bf1,bf2,bf3,bf4,bf5;
    //wel for welcome bf1 to bf 5 items

    Button bf1_inc = new Button("+");
    Button bf1_dec = new Button("-");
    TextField bf1_t = new TextField();

    public void init(){
        wel = getImage(getDocumentBase(),"wel.jpeg");
        bf1 = getImage(getDocumentBase(),"idli.jpeg");
        bf2 = getImage(getDocumentBase(),"dosa.jpeg");
        bf3 = getImage(getDocumentBase(),"wada.jpeg");
        bf4 = getImage(getDocumentBase(),"poori.jpeg");
        bf5 = getImage(getDocumentBase(),"upma.jpeg");
        
    }

    public void Pint(Graphics g){
        g.drawImage(wel,50,100,200,200,Color.red,this);
        g.drawImage(wel,110,100,200,200,Color.red,this);
        g.drawImage(wel,50,250,200,200,Color.red,this);
        g.drawImage(wel,110,250,200,200,Color.red,this);
        g.drawImage(wel,50,400,200,200,Color.red,this);
        g.drawImage(wel,110,400,200,200,Color.red,this);

    }
    @Override
    public void actionPerformed(ActionEvent e) {

    }

}
//<applet code="breakfast.class" width=1000 height=1000 ></applet>