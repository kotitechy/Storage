package java_programs1.src;
import java.util.Scanner;
class search1{
    Scanner sc =new Scanner(System.in);
    int i,l,h,m,k,n;
    int[] arr = new int[n];
    search(){
        System.out.println("Enter size of array: ");
        n = sc.nextInt();
    }
    void arr_in(){
        System.out.println("Enter " + n + "Elments: ");
                for(i=0;i<n;i++) {
                    System.out.println("a[" + i + "]");
                    arr[i] = sc.nextInt();
                }
        }
    void search_key() {
        System.out.println("Enter the key element to find: ");
        k =  sc.nextInt();
        l = 0;
        h = n-1;
        m = (h + l)/2;
        while(l <= h){
            if(arr[m] < k) {
                l = m + 1;
            }
            else if(arr[m] == k){
                System.out.println(k + " is an element of array");
                break;
            }
            else {
                h = m - 1;
                m = (l + h)/2;
            }
            if(l > h){
                System.out.println(k + " is not an element of array!..");
                return;
            }
        }
    }
    }

public class binary_search {
    public static int main(String[] args) {
search s1 = new search();
   s1.arr_in();
   s1.search_key();
   return 0;
    }
}
