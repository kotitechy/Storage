import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class Curries extends Applet implements ActionListener {

    int i=1;
    String msg="WELCOME";
    Button c_tc = new Button("Total");// total
    Button cls = new Button("Reset");
    TextField c_t = new TextField();// display total to all items

    Image wel, c1, c2, c3, c4, c5;
    // wel for welcome c1 to c5 items

    // array for curries
    int c_id[] = { 1, 2, 3, 4, 5 };// ID OF ITEMS
    String c_list[] = { "FULL MEAL", "CHICKEN", "MUTTON", "FISH", "PANEER" };// LIST OF ITEMS
    int c_p_items[] = { 60, 120, 200, 150, 100 };// price of items
    int q[] = new int[5]; // quantity of items
    int q_i[]; // setting quantity
    int price_total[] = new int[5];// mutiplying total
    int total;//total

    // full-meals inc,dec,textfield
    Button c1_inc = new Button("+");
    Button c1_dec = new Button("-");
    TextField c1_t = new TextField();

    // chicken inc,dec,textfield
    Button c2_inc = new Button("+");
    Button c2_dec = new Button("-");
    TextField c2_t = new TextField();

    // mutton inc,dec,textfield
    Button c3_inc = new Button("+");
    Button c3_dec = new Button("-");
    TextField c3_t = new TextField();

    // fish inc,dec,textfield
    Button c4_inc = new Button("+");
    Button c4_dec = new Button("-");
    TextField c4_t = new TextField();

    // paneer inc,dec,textfield
    Button c5_inc = new Button("+");
    Button c5_dec = new Button("-");
    TextField c5_t = new TextField();

    // total textfields
    TextField c1_p = new TextField();
    TextField c2_p = new TextField();
    TextField c3_p = new TextField();
    TextField c4_p = new TextField();
    TextField c5_p = new TextField();


 
    public void init() {

        wel = getImage(getDocumentBase(), "wel.jpeg");
        c1 = getImage(getDocumentBase(), "meal.jpg");
        c2 = getImage(getDocumentBase(), "chicken.jpg");
        c3 = getImage(getDocumentBase(), "mutton.jpg");
        c4 = getImage(getDocumentBase(), "fish.jpg");
        c5 = getImage(getDocumentBase(), "paneer.jpg");
        add(c1_inc);
        add(c2_inc);
        add(c3_inc);
        add(c4_inc);
        add(c5_inc);

        add(c1_dec);
        add(c2_dec);
        add(c3_dec);
        add(c4_dec);
        add(c5_dec);

        add(c1_t);
        add(c2_t);
        add(c3_t);
        add(c4_t);
        add(c5_t);

        add(c1_p);
        add(c2_p);
        add(c3_p);
        add(c4_p);
        add(c5_p);

        add(c_tc);
        add(c_t);
        add(cls);


        // adding action listener for l1_inc
        c1_inc.addActionListener(this);
        c2_inc.addActionListener(this);
        c3_inc.addActionListener(this);
        c4_inc.addActionListener(this);
        c5_inc.addActionListener(this);

        // adding action listener for l1_dec
        c1_dec.addActionListener(this);
        c2_dec.addActionListener(this);
        c3_dec.addActionListener(this);
        c4_dec.addActionListener(this);
        c5_dec.addActionListener(this);

        // adding action listener for total calc button
        c_tc.addActionListener(this);
        cls.addActionListener(this);



        setLayout(null);

        // button inc,dec of idli
        c1_inc.setBounds(100, 450, 50, 50);
        c1_dec.setBounds(250, 450, 50, 50);
        c1_t.setBounds(150, 450, 100, 50);

        // button inc,dec of dosa
        c2_inc.setBounds(350, 450, 50, 50);
        c2_dec.setBounds(500, 450, 50, 50);
        c2_t.setBounds(400, 450, 100, 50);

        // button inc,dec of wada
        c3_inc.setBounds(600, 450, 50, 50);
        c3_dec.setBounds(750, 450, 50, 50);
        c3_t.setBounds(650, 450, 100, 50);

        // button inc,dec of poori
        c4_inc.setBounds(850, 450, 50, 50);
        c4_dec.setBounds(1000, 450, 50, 50);
        c4_t.setBounds(900, 450, 100, 50);

        // button inc,dec of upma
        c5_inc.setBounds(1100, 450, 50, 50);
        c5_dec.setBounds(1250, 450, 50, 50);
        c5_t.setBounds(1150, 450, 100, 50);

        // textfield for total x quantity
        c1_p.setBounds(230, 520, 70, 42);
        c2_p.setBounds(480, 520, 70, 42);
        c3_p.setBounds(730, 520, 70, 42);
        c4_p.setBounds(980, 520, 70, 42);
        c5_p.setBounds(1230, 520, 70, 42);

        c_tc.setBounds(1030, 580, 50, 50);
        c_t.setBounds(1100,580,200,42);
        cls.setBounds(950, 580, 50, 50);

        

    }

    public void paint(Graphics g) {

        g.drawString(msg,150,580);

        g.drawRect(50, 20, 1300, 630);
        g.drawRect(250, 50, 300, 104);
        // image box
        g.drawRect(100, 200, 200, 200);
        g.drawRect(350, 200, 200, 200);
        g.drawRect(600, 200, 200, 200);
        g.drawRect(850, 200, 200, 200);
        g.drawRect(1100, 200, 200, 200);
        // images
        g.drawImage(wel, 250, 50, 300, 100, Color.red, this);
        g.drawImage(c1, 100, 200, 200, 200, Color.red, this);
        g.drawImage(c2, 350, 200, 200, 200, Color.red, this);
        g.drawImage(c3, 600, 200, 200, 200, Color.red, this);
        g.drawImage(c4, 850, 200, 200, 200, Color.red, this);
        g.drawImage(c5, 1100, 200, 200, 200, Color.red, this);

        // item name box
        g.drawRect(100, 520, 200, 40);
        g.drawRect(350, 520, 200, 40);
        g.drawRect(600, 520, 200, 40);
        g.drawRect(850, 520, 200, 40);
        g.drawRect(1100, 520, 200, 40);
        // item name
        g.drawString("MEALS   price: 60  Q: ", 101, 550);
        g.drawString("CHICKEN  price: 120  Q: ", 351, 550);
        g.drawString("MUTTON   price: 200  Q: ", 601, 550);
        g.drawString("FISH price: 150  Q: ", 851, 550);
        g.drawString("PANEER   price: 100  Q: ", 1101, 550);
        // box-1-main
        g.drawRect(100, 450, 200, 50);
        g.drawRect(350, 450, 200, 50);
        g.drawRect(600, 450, 200, 50);
        g.drawRect(850, 450, 200, 50);
        g.drawRect(1100, 450, 200, 50);

        // box-1-1
        g.drawRect(100, 450, 50, 50);
        g.drawRect(350, 450, 50, 50);
        g.drawRect(600, 450, 50, 50);
        g.drawRect(850, 450, 50, 50);
        g.drawRect(1100, 450, 50, 50);

        // box-1-1
        g.drawRect(100, 450, 150, 50);
        g.drawRect(350, 450, 150, 50);
        g.drawRect(600, 450, 150, 50);
        g.drawRect(850, 450, 150, 50);
        g.drawRect(1100, 450, 150, 50);

    }

    public void actionPerformed(ActionEvent e){
        //incrementing items in customer order array 

        if(e.getSource() == c1_inc){
           //String bf1_inc_t;
           q[0] = (q[0] + 1);
           String l1_inc_t = Integer.toString(q[0]);
           c1_t.setText(l1_inc_t);

           price_total[0] = q[0] * c_p_items[0];
           String p_t_1 = Integer.toString(price_total[0]);
           c1_p.setText(p_t_1);
           

        }

        
        if(e.getSource() == c2_inc){
            //String bf1_inc_t;
            q[1] = (q[1] + 1);
            String l2_inc_t = Integer.toString(q[1]);
            c2_t.setText(l2_inc_t);
            
            price_total[1] = q[1] * c_p_items[1];
           String p_t_2 = Integer.toString(price_total[1]);
           c2_p.setText(p_t_2);
        }

        if(e.getSource() == c3_inc){
            //String bf1_inc_t;
            q[2] = (q[2] + 1);
            String l3_inc_t = Integer.toString(q[2]);
            c3_t.setText(l3_inc_t);
            
            price_total[2] = q[2] * c_p_items[2];
           String p_t_3 = Integer.toString(price_total[2]);
           c3_p.setText(p_t_3);
        }
        
        if(e.getSource() == c4_inc){
            //String bf1_inc_t;
            q[3] = (q[3] + 1);
            String l4_inc_t = Integer.toString(q[3]);
            c4_t.setText(l4_inc_t);
            
            price_total[3] = q[3] * c_p_items[3];
           String p_t_4 = Integer.toString(price_total[3]);
           c4_p.setText(p_t_4);
        }
        
        if(e.getSource() == c5_inc){
            //String bf1_inc_t;
            q[4] = (q[4] + 1);
            String l5_inc_t = Integer.toString(q[4]);
            c5_t.setText(l5_inc_t);
            
            price_total[4] = q[4] * c_p_items[4];
           String p_t_5 = Integer.toString(price_total[4]);
           c5_p.setText(p_t_5);
        }

        //decrementing items in customer order array 

        if(e.getSource() == c1_dec){
            //String bf1_inc_t;
            q[0] = (q[0] - 1);
            String l1_inc_t = Integer.toString(q[0]);
            c1_t.setText(l1_inc_t);
            
            price_total[0] = q[0] * c_p_items[0];
           String p_t_1 = Integer.toString(price_total[0]);
           c1_p.setText(p_t_1);
        }

        
        if(e.getSource() == c2_dec){
            //String bf1_inc_t;
            q[1] = (q[1] - 1);
            String l2_inc_t = Integer.toString(q[1]);
            c2_t.setText(l2_inc_t);
            
            price_total[1] = q[1] * c_p_items[1];
           String p_t_2 = Integer.toString(price_total[1]);
           c2_p.setText(p_t_2);
        }

        if(e.getSource() == c3_dec){
            //String bf1_inc_t;
            q[2] = (q[2] - 1);
            String l3_inc_t = Integer.toString(q[2]);
            c3_t.setText(l3_inc_t);
            
            price_total[2] = q[2] * c_p_items[2];
           String p_t_3 = Integer.toString(price_total[2]);
           c3_p.setText(p_t_3);
        }
        
        if(e.getSource() == c4_dec){
            //String bf1_inc_t;
            q[3] = (q[3] - 1);
            String l4_inc_t = Integer.toString(q[3]);
            c4_t.setText(l4_inc_t);
            
             price_total[3] = q[3] * c_p_items[3];
           String p_t_4 = Integer.toString(price_total[3]);
           c4_p.setText(p_t_4);
        }
        
        if(e.getSource() == c5_dec){
            //String bf1_inc_t;
            q[4] = (q[4] - 1);
            String l5_inc_t = Integer.toString(q[4]);
            c5_t.setText(l5_inc_t);
            
            price_total[4] = q[4] * c_p_items[4];
           String p_t_5 = Integer.toString(price_total[4]);
           c5_p.setText(p_t_5);
        }
       if(e.getSource()==c_tc){
        for (int i = 0; i < c_id.length; i++) {
           total+= (price_total[i]);
        }
        String t = Integer.toString(total);
        c_t.setText(t);
}
if(e.getSource()== cls){  

    i = i + 1;

msg = " WELCOME " + i;
repaint();

   c1_p.setText("0");
   c2_p.setText("0");
   c3_p.setText("0");
   c4_p.setText("0");
   c5_p.setText("0");

   c1_t.setText("0");
   c2_t.setText("0");
   c3_t.setText("0");
   c4_t.setText("0");
   c5_t.setText("0");

   c_t.setText("0");
   
   total = 0; 

   for (int i = 0; i < 5; i++) {
    price_total[i] = 0;
   }

}
repaint();
}


}
// <applet code="Curries.class" width=2000 height=2000 ></applet>
//