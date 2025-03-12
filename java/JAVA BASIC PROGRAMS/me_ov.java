public class me_ov {
    public static void main(String[] args) {
        car c1 =new car();
        c1.details();
        c1.details("Bolero-ZLX",16);
        c1.details("TATA Nano","Petrol",18,4);
    }
}
class car{
    public void details(){
        System.out.println("Car Details \nName: Scorpio-N\nMilage: 24\ncapaity: 7-seater\nfuelType: Diesel");
    } 
    public void details(String name,int Milage){
        System.out.println("Car Details \nName: "+name+"\nMilage: "+Milage+"\ncapaity: 7-seater\nfuelType: Diesel");
    } 
    public void details(String name, String Fuel,int Milage,int cap){
        System.out.println("Car Details \nName: "+name+"\nMilage: "+Milage+"\ncapaity: "+cap+"\nfuelType: "+Fuel);
    }   
}