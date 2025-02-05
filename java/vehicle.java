public class vehicle {
    int vno,cap,l,mil;
    String vn;
    Double dis;
    public static void main(String[] args) {
        vehicle v1 = new vehicle();
        v1.vno=11;
        v1.cap=7;
        v1.vn="gclass";
        v1.l=50;
        v1.mil=16;
        v1.dis=(double)v1.l * v1.mil;
        System.out.println("Car Details: \nName:"+v1.vn+"\nNumber:"+v1.vno+"\nCapacity:"+v1.cap+"\nLiters:"+v1.l+"\nMilage:"+v1.mil+"\nDistance:"+v1.dis );
    }
}
