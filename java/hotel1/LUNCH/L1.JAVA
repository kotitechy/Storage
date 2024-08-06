import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class L1 extends Applet implements ActionListener {
    int i=1;
    String msg="WELCOME";
    Button l_tc = new Button("Total");// total
    Button cls = new Button("Reset");
    TextField l_t = new TextField();// display total to all items

    Image wel, l1, l2, l3, l4, l5;
    // wel for welcome l1 to l5 items

    // array for lunch
    int l_id[] = { 1, 2, 3, 4, 5 };// ID OF ITEMS
    String l_list[] = { "FULL MEAL", "CHICKEN", "MUTTON", "FISH", "PANEER" };// LIST OF ITEMS
    int l_p_items[] = { 60, 120, 200, 150, 100 };// price of items
    int q[] = new int[5]; // quantity of items
    int q_i[]; // setting quantity
    int price_total[] = new int[5];// mutiplying total
    int total;//total

    // full-meals inc,dec,textfield
    Button l1_inc = new Button("+");
    Button l1_dec = new Button("-");
    TextField l1_t = new TextField();

    // chicken inc,dec,textfield
    Button l2_inc = new Button("+");
    Button l2_dec = new Button("-");
    TextField l2_t = new TextField();

    // mutton inc,dec,textfield
    Button l3_inc = new Button("+");
    Button l3_dec = new Button("-");
    TextField l3_t = new TextField();

    // fish inc,dec,textfield
    Button l4_inc = new Button("+");
    Button l4_dec = new Button("-");
    TextField l4_t = new TextField();

    // paneer inc,dec,textfield
    Button l5_inc = new Button("+");
    Button l5_dec = new Button("-");
    TextField l5_t = new TextField();

    // total textfields
    TextField l1_p = new TextField();
    TextField l2_p = new TextField();
    TextField l3_p = new TextField();
    TextField l4_p = new TextField();
    TextField l5_p = new TextField();

    public void init() {

        wel = getImage(getDocumentBase(), "wel.jpeg");
        l1 = getImage(getDocumentBase(), "meal.jpg");
        l2 = getImage(getDocumentBase(), "chicken.jpg");
        l3 = getImage(getDocumentBase(), "mutton.jpg");
        l4 = getImage(getDocumentBase(), "fish.jpg");
        l5 = getImage(getDocumentBase(), "paneer.jpg");
        add(l1_inc);
        add(l2_inc);
        add(l3_inc);
        add(l4_inc);
        add(l5_inc);

        add(l1_dec);
        add(l2_dec);
        add(l3_dec);
        add(l4_dec);
        add(l5_dec);

        add(l1_t);
        add(l2_t);
        add(l3_t);
        add(l4_t);
        add(l5_t);

        add(l1_p);
        add(l2_p);
        add(l3_p);
        add(l4_p);
        add(l5_p);

        add(l_tc);
        add(l_t);
        add(cls);



        setLayout(null);

        // button inc,dec of idli
        l1_inc.setBounds(100, 450, 50, 50);
        l1_dec.setBounds(250, 450, 50, 50);
        l1_t.setBounds(150, 450, 100, 50);

        // button inc,dec of dosa
        l2_inc.setBounds(350, 450, 50, 50);
        l2_dec.setBounds(500, 450, 50, 50);
        l2_t.setBounds(400, 450, 100, 50);

        // button inc,dec of wada
        l3_inc.setBounds(600, 450, 50, 50);
        l3_dec.setBounds(750, 450, 50, 50);
        l3_t.setBounds(650, 450, 100, 50);

        // button inc,dec of poori
        l4_inc.setBounds(850, 450, 50, 50);
        l4_dec.setBounds(1000, 450, 50, 50);
        l4_t.setBounds(900, 450, 100, 50);

        // button inc,dec of upma
        l5_inc.setBounds(1100, 450, 50, 50);
        l5_dec.setBounds(1250, 450, 50, 50);
        l5_t.setBounds(1150, 450, 100, 50);

        // textfield for total x quantity
        l1_p.setBounds(230, 520, 70, 42);
        l2_p.setBounds(480, 520, 70, 42);
        l3_p.setBounds(730, 520, 70, 42);
        l4_p.setBounds(980, 520, 70, 42);
        l5_p.setBounds(1230, 520, 70, 42);

        l_tc.setBounds(1030, 580, 50, 50);
        l_t.setBounds(1100,580,200,42);
        cls.setBounds(950, 580, 50, 50);

        // adding action listener for l1_inc
        l1_inc.addActionListener(this);
        l2_inc.addActionListener(this);
        l3_inc.addActionListener(this);
        l4_inc.addActionListener(this);
        l5_inc.addActionListener(this);

        // adding action listener for l1_dec
        l1_dec.addActionListener(this);
        l2_dec.addActionListener(this);
        l3_dec.addActionListener(this);
        l4_dec.addActionListener(this);
        l5_dec.addActionListener(this);

        // adding action listener for total calc button
        l_tc.addActionListener(this);
        cls.addActionListener(this);

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
        g.drawImage(l1, 100, 200, 200, 200, Color.red, this);
        g.drawImage(l2, 350, 200, 200, 200, Color.red, this);
        g.drawImage(l3, 600, 200, 200, 200, Color.red, this);
        g.drawImage(l4, 850, 200, 200, 200, Color.red, this);
        g.drawImage(l5, 1100, 200, 200, 200, Color.red, this);

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

        if(e.getSource() == l1_inc){
           //String bf1_inc_t;
           q[0] = (q[0] + 1);
           String l1_inc_t = Integer.toString(q[0]);
           l1_t.setText(l1_inc_t);

           price_total[0] = q[0] * l_p_items[0];
           String p_t_1 = Integer.toString(price_total[0]);
           l1_p.setText(p_t_1);
           

        }

        
        if(e.getSource() == l2_inc){
            //String bf1_inc_t;
            q[1] = (q[1] + 1);
            String l2_inc_t = Integer.toString(q[1]);
            l2_t.setText(l2_inc_t);
            
            price_total[1] = q[1] * l_p_items[1];
           String p_t_2 = Integer.toString(price_total[1]);
           l2_p.setText(p_t_2);
        }

        if(e.getSource() == l3_inc){
            //String bf1_inc_t;
            q[2] = (q[2] + 1);
            String l3_inc_t = Integer.toString(q[2]);
            l3_t.setText(l3_inc_t);
            
            price_total[2] = q[2] * l_p_items[2];
           String p_t_3 = Integer.toString(price_total[2]);
           l3_p.setText(p_t_3);
        }
        
        if(e.getSource() == l4_inc){
            //String bf1_inc_t;
            q[3] = (q[3] + 1);
            String l4_inc_t = Integer.toString(q[3]);
            l4_t.setText(l4_inc_t);
            
            price_total[3] = q[3] * l_p_items[3];
           String p_t_4 = Integer.toString(price_total[3]);
           l4_p.setText(p_t_4);
        }
        
        if(e.getSource() == l5_inc){
            //String bf1_inc_t;
            q[4] = (q[4] + 1);
            String l5_inc_t = Integer.toString(q[4]);
            l5_t.setText(l5_inc_t);
            
            price_total[4] = q[4] * l_p_items[4];
           String p_t_5 = Integer.toString(price_total[4]);
           l5_p.setText(p_t_5);
        }

        //decrementing items in customer order array 

        if(e.getSource() == l1_dec){
            //String bf1_inc_t;
            q[0] = (q[0] - 1);
            String l1_inc_t = Integer.toString(q[0]);
            l1_t.setText(l1_inc_t);
            
            price_total[0] = q[0] * l_p_items[0];
           String p_t_1 = Integer.toString(price_total[0]);
           l1_p.setText(p_t_1);
        }

        
        if(e.getSource() == l2_dec){
            //String bf1_inc_t;
            q[1] = (q[1] - 1);
            String l2_inc_t = Integer.toString(q[1]);
            l2_t.setText(l2_inc_t);
            
            price_total[1] = q[1] * l_p_items[1];
           String p_t_2 = Integer.toString(price_total[1]);
           l2_p.setText(p_t_2);
        }

        if(e.getSource() == l3_dec){
            //String bf1_inc_t;
            q[2] = (q[2] - 1);
            String l3_inc_t = Integer.toString(q[2]);
            l3_t.setText(l3_inc_t);
            
            price_total[2] = q[2] * l_p_items[2];
           String p_t_3 = Integer.toString(price_total[2]);
           l3_p.setText(p_t_3);
        }
        
        if(e.getSource() == l4_dec){
            //String bf1_inc_t;
            q[3] = (q[3] - 1);
            String l4_inc_t = Integer.toString(q[3]);
            l4_t.setText(l4_inc_t);
            
             price_total[3] = q[3] * l_p_items[3];
           String p_t_4 = Integer.toString(price_total[3]);
           l4_p.setText(p_t_4);
        }
        
        if(e.getSource() == l5_dec){
            //String bf1_inc_t;
            q[4] = (q[4] - 1);
            String l5_inc_t = Integer.toString(q[4]);
            l5_t.setText(l5_inc_t);
            
            price_total[4] = q[4] * l_p_items[4];
           String p_t_5 = Integer.toString(price_total[4]);
           l5_p.setText(p_t_5);
        }
       if(e.getSource()==l_tc){
        for (int i = 0; i < l_id.length; i++) {
           total+= (price_total[i]);
        }
        String t = Integer.toString(total);
        l_t.setText(t);
}
if(e.getSource()== cls){  

    i = i + 1;

msg = " WELCOME " + i;
repaint();

   l1_p.setText("0");
   l2_p.setText("0");
   l3_p.setText("0");
   l4_p.setText("0");
   l5_p.setText("0");

   l1_t.setText("0");
   l2_t.setText("0");
   l3_t.setText("0");
   l4_t.setText("0");
   l5_t.setText("0");

   l_t.setText("0");
   
   total = 0; 

   for (int i = 0; i < 5; i++) {
    price_total[i] = 0;
   }

}
repaint();
}
}
// <applet code="L1.class" width=2000 height=2000 ></applet>
//