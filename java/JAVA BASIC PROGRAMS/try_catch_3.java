import java.util.Scanner;

public class try_catch_3 {
    public static void main(String[] args) {
        int m[] = new int[100];
//        m[0]=10;
//        m[1]=20;
//        m[2]=30;
//        m[3]=40;
//        m[4]=50;
        Scanner sc = new Scanner(System.in);

        try{
            System.out.println("Welcome");

            try{
//                System.out.println(m[a]);
                int i=1;
                while(true){
                    System.out.println("\n 1. add 2. see");
                    int ch = sc.nextInt();
                switch (ch){
                    case 1:
                        System.out.println("Enter the value ");
                        m[i] = sc.nextInt();
                        System.out.println("Successfully added a element " + m[i]);
                        i++;
                        break;

                    case 2:

                        for(int j=0;j<=i;j++){
                            System.out.print(m[j] + "  ");

                        }
                }
                }

            }
            catch (ArrayIndexOutOfBoundsException e){
                System.out.println("Sorry this index doesn't exists");
                System.out.println("Exception in level-2");
            }
        }
        catch(Exception e){
            System.out.println("Exception to level-1");
        }
        System.out.println(123);
    }
    /*
    quick quiz
   program to access the array values until the limited index
     */
}
