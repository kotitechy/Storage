public class Primes {
    public static void main(String[] args) {
        int n = 20;
        int c = 0;
        for (int j = 2; j < n; j++) {
            boolean isp = true;
            for (int i = 2; i < j; i++) {
                if (j % i == 0) {
                    isp = false;
                    break;
                }
            }
            if (isp) {
                System.out.println(j + "is Prime!");
                c += 1;
            }
        }
        System.out.println("Count: " + c);
    }
}
