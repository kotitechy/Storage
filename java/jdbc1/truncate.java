import java.sql.*;


public class truncate {
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

         String q = "truncate employee";
         Statement stmt = con.createStatement();

         stmt.executeUpdate(q);
         System.out.println("data has been deleted from table");

        } catch (Exception e) {
            // TODO: handle exception
        }

    

}    
}
