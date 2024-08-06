class a{
    public:
    int x;
}
class b extends a{
    public:
    int y;
}
class c extends c{
    public:
    int z;
    c(int a,int b){
        super (x);
        super (y);
        a = x;
        b = y;
    }
    void add(int a ,int b){
System.out.println("The sum of " + x " and " + y + "is " + (x + y));
    }
    
}
class hirar_inherit{
    public static void main(){
        c ob = new c(10,20);
        ob.add(10,20);
    }
}