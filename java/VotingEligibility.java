import java.util.Scanner;

class VotingEligibilityException extends Exception {
	public VotingEligibilityException(String m){
		System.out.println(m);
	}
	
}

public class VotingEligibility {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        try {
            int age = scanner.nextInt();
            try{
            if(age>=18) 
            if(age<=60){
                System.out.println("eligible to vote");
			}
            if(age>60 || age<18){
                throw new VotingEligibilityException("Age must be Between 18 and 60");
			}
        }  catch (VotingEligibilityException e) {
        }
    }catch (Exception    e) {
        System.out.println("Ivalid input");
       }
          finally {
            scanner.close();
        }
    }
}
