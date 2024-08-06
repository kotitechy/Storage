

import java.sql.*;

class P1{
    public static void main(String [] args){
        try{
//load the driver
         Class.forName("com.mysql.cj.jdbc.Driver");
        
         //creating a connection
         String url = "jdbc:mysql://localhost:3306";
         String username = "root";
         String password = "root";

         Connection con = DriverManager.getConnection(url, username, password);

         if(con.isClosed()){
            System.out.println("Connection is Still closed");
         }
         else{
            System.out.println("Connection created...");
            String st1 = " create database atm";
    
            //create statement
            Statement stmt1 = con.createStatement();

            stmt1.executeUpdate(st1);
          System.out.println("Ceated student table");
            con.close();
         }


        }
        catch(Exception e){
            e.printStackTrace();
        }
    }
}