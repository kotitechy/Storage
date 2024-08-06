import java.awt.*;
import java.applet.*;
import java.awt.event.*;


public class Ap1 extends Applet implements ActionListener{
String msg="CALUCLATOR";
TextField t1 = new TextField(20);
TextField t2 = new TextField(20);
TextField t3 = new TextField(20);

Button b1 = new Button("Add");
Button b2 = new Button("Sub");
Button b3 = new Button("Mul");
Button b4 = new Button("Div");
Button b5 = new Button("Mod");
Button b6 = new Button("Reset");
Button b7 = new Button("");


public void init(){
add(t1);
add(t2);
add(t3);

add(b1);
add(b2);
add(b3);
add(b4);
add(b5);
add(b6);
add(b7);

b1.addActionListener(this);
b2.addActionListener(this);
b3.addActionListener(this);
b4.addActionListener(this);
b5.addActionListener(this);
b6.addActionListener(this);
b7.addActionListener(this);


}
public void paint(Graphics g){
g.drawString(msg,100,100);
}
public void actionPerformed(ActionEvent e){
double a=0,b=0,c=0;
try{
	a = Double.parseDouble(t1.getText());
}
catch(NumberFormatException Ae){
	t1.setText("Invalid Text");
}
try{
	b = Double.parseDouble(t2.getText());
}
catch(NumberFormatException Ae){
	t2.setText("Invalid Text");
}
if(e.getSource()==b1){
	c = b + a;
	t3.setText(String.valueOf(c));
	msg="ADDED";
}
if(e.getSource()==b2){
	c = a - b;
	t3.setText(String.valueOf(c));
	msg="SUBTRACTED";
}

if(e.getSource()==b3){
	c = a * b;
	t3.setText(String.valueOf(c));
	msg="MULTIPLIED";
}

if(e.getSource()==b5){
	c = a / b;
	t3.setText(String.valueOf(c));
	msg="DIVIDED";
}
if(e.getSource()==b1){
	c = a % b;
	t3.setText(String.valueOf(c));
	msg="MODULI DIVISION";
}

if(e.getSource()==b6){
	t1.setText("");
	t2.setText("");
	t3.setText("");
	msg="RESETED";
}
if(e.getSource()==b7){
	System.exit(0);
	msg="EXITING SYSTEM";
}

//repaint();
}
}
//<Applet code="Ap1.class" width=200 height=200></Applet>