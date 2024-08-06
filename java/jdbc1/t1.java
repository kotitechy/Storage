import java.sql.*;


public class t1 {
public static void main(String[] args) {
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
           }

         String q = "create table employee12(id int(30) primary key auto_increment,name varchar(30) not null,email varchar(50) not null ,city varchar(50));"; 

         Statement stmt = con.createStatement();

         stmt.executeUpdate(q);
         System.out.println("table has been created");

        } catch (Exception e) {
            // TODO: handle exception
        }

    

}    
}
