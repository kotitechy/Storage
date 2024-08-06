import java.util.Scanner;

class hotel{
int items[]={1,2,3,4,5};//id
String list[]={"IDLI","DOSA","WADA","BONDA","POORI"};//items
int price[]={30,45,35,30,40};//price of items

public void menu(){
    System.out.println("BREAK_FAST MENU LIST \n1. IDLI 2. DOSA 3. WADA 4. BONDA 5.POORI");
}
}
public class h1 extends hotel{
    Scanner sc = new Scanner(System.in);
      int order[] = new int[5];
      //int [] pid;
      int pp[] = {30,45,35,30,40};
      double total=0;

      public void getorderlist(){
        for(int i=0;i<5;i++){
            order[i] = 0;
          }
      for(int i=0;i<5;i++){
        System.out.println("Enter " + list[i] + " in number");
        order[i] = sc.nextInt();
      }
    }
    

    public void multiply1(){
          int op[] = new int[5];
        try{
        for(int i=0;i<5;i++){
            op[i]=( pp[i] * order[i] );
            total+=op[i];

        }
            System.out.println("ORDER DETAILS ");
            System.out.println("|------|---------|------------|--------|");
            System.out.println("| SNO  | ITEM    | QUANTITY   | PRICE per piece |  total price");
            for (int i = 0; i < 5; i++) {
                System.out.println(" "+(i+1) + ".  | "+list[i]+"   | "+ order[i]+"   | "+price[i]+" |"+op[i]);
                            }
            System.out.println("|------|---------|------------|--------|");
            System.out.println("TOTAL : " + total);

    }
    catch(Exception e){
        System.out.println(e);
    }

    }
      //int noi = sc.nextInt();
      //
     //


    public static void main(String[] args) {
        h1 ob = new h1();
        ob.getorderlist();
        ob.multiply1();
    }
}