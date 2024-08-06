
public class sorting_city  {
    //sorting the array ofString elements according to the alphabet order
    public static void main(String[] args) {
        String s1[] = {"delhi","agra","canada","zimbombae","india","yak"};
        int n  = s1.length;
        String t = null;
        for (int i = 0; i < n; i++) {
            for (int j =i+1; j <n ; j++) {
                if(s1[j].compareTo(s1[i])<0){
                    t = s1[i];
                    s1[i] = s1[j];
                    s1[j] = t;
                }

            }

        }
        System.out.println("City name are");
        for (int i = 0; i < n; i++) {
            System.out.println(s1[i]);

        }
    }
    

}
