import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class main {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/db1";
        String user = "root";
        String password = "root";

        // JDBC connection
        try (Connection conn = DriverManager.getConnection(url, user, password);
                Statement stmt = conn.createStatement()) {

            System.out.println("Connected to the database successfully!");

            // Insert data into student table
            try {
                stmt.executeUpdate("INSERT INTO student (id, name, branch) VALUES (1, 'shiva', 'cse')");
                System.out.println("Data inserted successfully!");
            } catch (Exception e) {
                System.out.println("Error in inserting data: " + e.getMessage());
            }

            // Retrieve and display student table data
            ResultSet rs = stmt.executeQuery("SELECT * FROM student");
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                String branch = rs.getString("branch");
                System.out.println("ID: " + id + ", Name: " + name + ", Branch: " + branch);
            }

        } catch (SQLException e) {
            System.out.println("Database connection failed!");
            e.printStackTrace();
        }
    }
}