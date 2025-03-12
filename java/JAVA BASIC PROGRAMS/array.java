import java.util.Scanner;

public class array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no of rows: ");
        int a = sc.nextInt();
        System.out.print("Enter no of columns: ");
        int b = sc.nextInt();
        int ma[][]=new int[a][b];
        int mb[][]=new int[a][b];
        int mc[][]=new int[a][b];
        // inputs
        System.out.println("ENter Matrix A");
        for(int i =0;i<a;i++){
        for(int j =0;j<b;j++){
            ma[i][j]=sc.nextInt();
            // mb[i][j]=sc.nextInt();
        }
    }
    System.out.println("ENter Matrix B");
        for(int i =0;i<a;i++){
        for(int j =0;j<b;j++){
            // ma[i][j]=sc.nextInt();
            mb[i][j]=sc.nextInt();
        }
    }
    if(a==b){
    for(int i =0;i<a;i++){
        for(int j =0;j<b;j++){
            mc[i][j]+=ma[i][j]*mb[i][j];
        }
    }
 
}
System.out.println("Matrix After Mul: ");
for(int i =0;i<a;i++){
    for(int j =0;j<b;j++){
        System.out.print(mc[i][j]+" ");
    }
    System.out.println();
}

}
}
