import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;

public class main extends Applet implements ActionListener {
    Button bf_tc = new Button("Total");// total
    Button cls = new Button("Reset");
    TextField bf_t = new TextField();// display total to all items

    Scrollbar s = new Scrollbar(); 
    int i = 1;
    String msg="WELCOME" + i;

    Image wel, bf1, bf2, bf3, bf4, bf5;
    // wel for welcome bf1 to bf 5 items

    // array for breakfast
    int bf_id[] = { 1, 2, 3, 4, 5 };// ID OF ITEMS
    String bf_list[] = { "IDLI", "DOSA", "WADA", "POORI", "UPMA" };// LIST OF ITEMS
    int bf_p_items[] = { 35, 40, 35, 30, 50 };// price of items
    int q[] = new int[5]; // quantity of items
    int q_i[]; // setting quantity
    int price_total[] = new int[5];// mutiplying total
    int total;//total


    //login
    TextField t1 = new TextField(20);//name
    TextField t2 = new TextField(20);//pinno
    TextField t3 = new TextField(20);//marks
    FlowLayout gr1 = new FlowLayout(FlowLayout.LEFT);
    Label l1 = new Label("NAME   : ");
    Label l2 = new Label("PIN-NO : ");
    Label l3 = new Label("MARKS  : ");
    Label l4 = new Label("GENDER : ");
    Label l5 = new Label("AGE    : ");


    Choice c = new Choice();



Button b1 = new Button("SUBMIT");
static String s1="";
static String s2="";
static String s3="";
static String gen;
static String age;


CheckboxGroup gender = new CheckboxGroup();
Checkbox m = new Checkbox("MALE",gender,true);
Checkbox f = new Checkbox("FEMALE",gender,false);
Checkbox o = new Checkbox("OTHERS",gender,false);



    // idli inc,dec,textfield
    Button bf1_inc = new Button("+");
    Button bf1_dec = new Button("-");
    TextField bf1_t = new TextField();

    // dosa inc,dec,textfield
    Button bf2_inc = new Button("+");
    Button bf2_dec = new Button("-");
    TextField bf2_t = new TextField();

    // wada inc,dec,textfield
    Button bf3_inc = new Button("+");
    Button bf3_dec = new Button("-");
    TextField bf3_t = new TextField();

    // poori inc,dec,textfield
    Button bf4_inc = new Button("+");
    Button bf4_dec = new Button("-");
    TextField bf4_t = new TextField();

    // upma inc,dec,textfield
    Button bf5_inc = new Button("+");
    Button bf5_dec = new Button("-");
    TextField bf5_t = new TextField();

    // total textfields
    TextField bf1_p = new TextField();
    TextField bf2_p = new TextField();
    TextField bf3_p = new TextField();
    TextField bf4_p = new TextField();
    TextField bf5_p = new TextField();


    public void init() {

        add(l1);//name
add(t1);

add(l2);//pinno
add(t2);

add(l3);//marks
add(t3);
        add(l4);//age
        c.add("AGE");
        c.add("15");
        c.add("16");
        c.add("17");
        c.add("18");
        c.add("19");
        c.add("20");
        c.add("21");
        add(c);
    
        add(m);
        add(f);
        add(o);
    
    add(b1);//submit
    b1.addActionListener(this);


    
        wel = getImage(getDocumentBase(), "wel.jpeg");
        bf1 = getImage(getDocumentBase(), "idli.jpeg");
        bf2 = getImage(getDocumentBase(), "dosa.jpeg");
        bf3 = getImage(getDocumentBase(), "wada.jpeg");
        bf4 = getImage(getDocumentBase(), "poori.jpeg");
        bf5 = getImage(getDocumentBase(), "upma.jpeg");
        add(bf1_inc);
        add(bf2_inc);
        add(bf3_inc);
        add(bf4_inc);
        add(bf5_inc);

        add(bf1_dec);
        add(bf2_dec);
        add(bf3_dec);
        add(bf4_dec);
        add(bf5_dec);

        add(bf1_t);
        add(bf2_t);
        add(bf3_t);
        add(bf4_t);
        add(bf5_t);

        add(bf1_p);
        add(bf2_p);
        add(bf3_p);
        add(bf4_p);
        add(bf5_p);

        add(bf_tc);
        add(bf_t);
        add(cls);

        add(s);

        setLayout(null);

        // button inc,dec of idli
        bf1_inc.setBounds(100, 450, 50, 50);
        bf1_dec.setBounds(250, 450, 50, 50);
        bf1_t.setBounds(150, 450, 100, 50);

        // button inc,dec of dosa
        bf2_inc.setBounds(350, 450, 50, 50);
        bf2_dec.setBounds(500, 450, 50, 50);
        bf2_t.setBounds(400, 450, 100, 50);

        // button inc,dec of wada
        bf3_inc.setBounds(600, 450, 50, 50);
        bf3_dec.setBounds(750, 450, 50, 50);
        bf3_t.setBounds(650, 450, 100, 50);

        // button inc,dec of poori
        bf4_inc.setBounds(850, 450, 50, 50);
        bf4_dec.setBounds(1000, 450, 50, 50);
        bf4_t.setBounds(900, 450, 100, 50);

        // button inc,dec of upma
        bf5_inc.setBounds(1100, 450, 50, 50);
        bf5_dec.setBounds(1250, 450, 50, 50);
        bf5_t.setBounds(1150, 450, 100, 50);

        // textfield for total x quantity
        bf1_p.setBounds(230, 520, 70, 42);
        bf2_p.setBounds(480, 520, 70, 42);
        bf3_p.setBounds(730, 520, 70, 42);
        bf4_p.setBounds(980, 520, 70, 42);
        bf5_p.setBounds(1230, 520, 70, 42);

        bf_tc.setBounds(1030, 580, 50, 50);
        bf_t.setBounds(1100,580,200,42);
        cls.setBounds(950, 580, 50, 50);

        // adding action listener for bf1_inc
        bf1_inc.addActionListener(this);
        bf2_inc.addActionListener(this);
        bf3_inc.addActionListener(this);
        bf4_inc.addActionListener(this);
        bf5_inc.addActionListener(this);

        // adding action listener for bf1_dec
        bf1_dec.addActionListener(this);
        bf2_dec.addActionListener(this);
        bf3_dec.addActionListener(this);
        bf4_dec.addActionListener(this);
        bf5_dec.addActionListener(this);

        // adding action listener for total calc button
        bf_tc.addActionListener(this);
        cls.addActionListener(this);

        
    s.setBounds (10, 800, 10, 20);

    

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
        g.drawImage(bf1, 100, 200, 200, 200, Color.red, this);
        g.drawImage(bf2, 350, 200, 200, 200, Color.red, this);
        g.drawImage(bf3, 600, 200, 200, 200, Color.red, this);
        g.drawImage(bf4, 850, 200, 200, 200, Color.red, this);
        g.drawImage(bf5, 1100, 200, 200, 200, Color.red, this);

        // item name box
        g.drawRect(100, 520, 200, 40);
        g.drawRect(350, 520, 200, 40);
        g.drawRect(600, 520, 200, 40);
        g.drawRect(850, 520, 200, 40);
        g.drawRect(1100, 520, 200, 40);
        // item name
        g.drawString("IDLI   price: 35  Q: ", 101, 550);
        g.drawString("DOSA   price: 40  Q: ", 351, 550);
        g.drawString("WADA   price: 35  Q: ", 601, 550);
        g.drawString("POORI  price: 30  Q: ", 851, 550);
        g.drawString("UPMA   price: 50  Q: ", 1101, 550);
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

        if(e.getSource() == bf1_inc){
           //String bf1_inc_t;
           q[0] = (q[0] + 1);
           String bf1_inc_t = Integer.toString(q[0]);
           bf1_t.setText(bf1_inc_t);

           price_total[0] = q[0] * bf_p_items[0];
           String p_t_1 = Integer.toString(price_total[0]);
           bf1_p.setText(p_t_1);
           

        }

        
        if(e.getSource() == bf2_inc){
            //String bf1_inc_t;
            q[1] = (q[1] + 1);
            String bf2_inc_t = Integer.toString(q[1]);
            bf2_t.setText(bf2_inc_t);
            
            price_total[1] = q[1] * bf_p_items[1];
           String p_t_2 = Integer.toString(price_total[1]);
           bf2_p.setText(p_t_2);
        }

        if(e.getSource() == bf3_inc){
            //String bf1_inc_t;
            q[2] = (q[2] + 1);
            String bf3_inc_t = Integer.toString(q[2]);
            bf3_t.setText(bf3_inc_t);
            
            price_total[2] = q[2] * bf_p_items[2];
           String p_t_3 = Integer.toString(price_total[2]);
           bf3_p.setText(p_t_3);
        }
        
        if(e.getSource() == bf4_inc){
            //String bf1_inc_t;
            q[3] = (q[3] + 1);
            String bf4_inc_t = Integer.toString(q[3]);
            bf4_t.setText(bf4_inc_t);
            
            price_total[3] = q[3] * bf_p_items[3];
           String p_t_4 = Integer.toString(price_total[3]);
           bf4_p.setText(p_t_4);
        }
        
        if(e.getSource() == bf5_inc){
            //String bf1_inc_t;
            q[4] = (q[4] + 1);
            String bf5_inc_t = Integer.toString(q[4]);
            bf5_t.setText(bf5_inc_t);
            
            price_total[4] = q[4] * bf_p_items[4];
           String p_t_5 = Integer.toString(price_total[4]);
           bf5_p.setText(p_t_5);
        }

        //decrementing items in customer order array 

        if(e.getSource() == bf1_dec){
            //String bf1_inc_t;
            q[0] = (q[0] - 1);
            String bf1_inc_t = Integer.toString(q[0]);
            bf1_t.setText(bf1_inc_t);
            
            price_total[0] = q[0] * bf_p_items[0];
           String p_t_1 = Integer.toString(price_total[0]);
           bf1_p.setText(p_t_1);
        }

        
        if(e.getSource() == bf2_dec){
            //String bf1_inc_t;
            q[1] = (q[1] - 1);
            String bf2_inc_t = Integer.toString(q[1]);
            bf2_t.setText(bf2_inc_t);
            
            price_total[1] = q[1] * bf_p_items[1];
           String p_t_2 = Integer.toString(price_total[1]);
           bf2_p.setText(p_t_2);
        }

        if(e.getSource() == bf3_dec){
            //String bf1_inc_t;
            q[2] = (q[2] - 1);
            String bf3_inc_t = Integer.toString(q[2]);
            bf3_t.setText(bf3_inc_t);
            
            price_total[2] = q[2] * bf_p_items[2];
           String p_t_3 = Integer.toString(price_total[2]);
           bf3_p.setText(p_t_3);
        }
        
        if(e.getSource() == bf4_dec){
            //String bf1_inc_t;
            q[3] = (q[3] - 1);
            String bf4_inc_t = Integer.toString(q[3]);
            bf4_t.setText(bf4_inc_t);
            
             price_total[3] = q[3] * bf_p_items[3];
           String p_t_4 = Integer.toString(price_total[3]);
           bf4_p.setText(p_t_4);
        }
        
        if(e.getSource() == bf5_dec){
            //String bf1_inc_t;
            q[4] = (q[4] - 1);
            String bf5_inc_t = Integer.toString(q[4]);
            bf5_t.setText(bf5_inc_t);
            
            price_total[4] = q[4] * bf_p_items[4];
           String p_t_5 = Integer.toString(price_total[4]);
           bf5_p.setText(p_t_5);
        }
       if(e.getSource()==bf_tc){
        for (int i = 0; i < bf_id.length; i++) {
           total+= (price_total[i]);
        }
        String t = Integer.toString(total);
        bf_t.setText(t);
}
if(e.getSource()== cls){  

    i = i + 1;

msg = " WELCOME " + i;
repaint();

   bf1_p.setText("0");
   bf2_p.setText("0");
   bf3_p.setText("0");
   bf4_p.setText("0");
   bf5_p.setText("0");

   bf1_t.setText("0");
   bf2_t.setText("0");
   bf3_t.setText("0");
   bf4_t.setText("0");
   bf5_t.setText("0");

   bf_t.setText("0");
   
   total = 0; 

   for (int i = 0; i < 5; i++) {
    price_total[i] = 0;
   }

}
s1 = t1.getText();
s2 = t2.getText();
s3 = t3.getText();
gen = gender.getSelectedCheckbox().getLabel();
age = c.getSelectedItem();
repaint();
}
}

// <applet code="main.class" width=2000 height=2000 ></applet>
// 