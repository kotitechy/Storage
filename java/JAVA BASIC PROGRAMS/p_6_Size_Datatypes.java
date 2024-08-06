//Know the size of the data-types
// Mainly using 1. MIN_VALUE 2. MAX_VALUE
class p_6_Size_Datatypes{
public static void main(String [] agrs){
//Integer
int a = 10;  //int
float b = 2.22f;  //float
double d = 12.2344d;   //double
long l = 123456789;   //long
byte by = 7;     //byte
short s = 12;  //short
//Non-Integer
char ch = 's';    //char
String name = " Shiva ";   //String


System.out.println("Integer");
System.out.println("Int     : " + int.MAX_VALUE);
System.out.println("Float   : " + float.MAX_VALUE);
System.out.println("Long    : " + long.MAX_VALUE);
System.out.println("Short   : " + short.MAX_VALUE);
System.out.println("Byte    : " + byte.MAX_VALUE);

System.out.println("Non-Integer : ");
System.out.println("Char    : " + char.MAX_VALUE);
System.out.println("String  : " + name.MAX_VALUE);

}
}
