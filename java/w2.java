class w2{
    public static void main(String[] args) {
        int n1 = Integer.parseInt(args[0]);
        int n2 = Integer.parseInt(args[1]);
        total(n1,n2);
    }
    public static void total(int t1,int t2){
        System.out.println("Total: "+(t1+t2));
        System.out.println("Avg: "+(t1+t2)/2);
    }
}