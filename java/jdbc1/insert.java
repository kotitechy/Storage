import java.net.ConnectException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.Scanner;

public class insert {
    public static void main(String[] args) {
        java.util.Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name: ");
        String name = sc.nextLine();
        System.out.println("Enter your emailid: ");
        String email = sc.nextLine();
        System.out.println("Enter your city: ");
        String city = sc.nextLine();
        System.out.println("Enter your id: ");
        int id = sc.nextInt();

            try {
            Class.forName("com.mysql.jdbc.Driver");
            
            String url ="jdbc:mysql://103.125.163.18:3306/db1";
            String username="root";
            String password = "root";

           Connection con = DriverManager.getConnection(url,username,password);

           if(con.isClosed()){
            System.out.println("Connection is closed");
         
           }
           else{
            System.out.println("connection is open");
            String q = "insert into employee(id,name,email,city) values(?,?,?,?)";
         PreparedStatement stmt1 = con.prepareStatement(q);
        stmt1.setInt(1, id);
         stmt1.setString(2, name);
         stmt1.setString(3,email);
         stmt1.setString(4,city);

         stmt1.executeUpdate();

         System.out.println("data has been inserted");   
         
         con.close();
             
         

           }
           
         

       

        }catch(Exception e){
System.out.println("error");
        }
    }
    }
