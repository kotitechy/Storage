public class md_array {
    public static void main(String[] args) {
        int[][][] arr = {
                {{1,2,3},{10,20,30},{11,12,13}}
        };
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                for (int k = 0; k < arr[i][j].length; k++) {
                    System.out.print(
                            arr[0][0][0] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
    }
}
