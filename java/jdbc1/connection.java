import java.sql.*;

public class connection{ 
              public static void main(String[] args) {
                
            
           
           try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            String url ="jdbc:mysql://local/db1";
            String username="root";
            String password = "root";

           Connection con = DriverManager.getConnection(url,username,password);

           if(con.isClosed()){
            System.out.println("Connection is closed");
            //  return "Connection is closed";

           }
           else{
            System.out.println("connection is open");
           }

          

        } catch (Exception e) {
            // TODO: handle exception
            System.out.println("Error ");
        }
        // return "Function sucess";
    }
}
