/*Datatypes in java
Data types 
1. Primitive 2. Non-Primitive

===>> a. primitive   1. integer 2. non integer
=> 1. integer
       a. int ,b. float ,c. long ,d. double ,e. short ,f. byte
=> 2. non Integer types  
       a. Boolean ,b. char ,c. String
===>>> b. non-primitive 
       a. array ,b. objects
*/
class p_5_DataTypes {
public static void main(String [] args){
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

//non-primitive 
int arr []= {10,20,30,40,50,60,70};

//Boolean
boolean b1 = true;
System.out.println("Integer");
System.out.println("Int     : " + a);
System.out.println("Float   : " + b);
System.out.println("Long    : " + l);
System.out.println("Short   : " + s);
System.out.println("Byte    : " + by);
System.out.println("Non-Integer : ");
System.out.println("Char    : " + ch);
System.out.println("String  : " + name);

//non-primitive
System.out.print("Array   : ");
for(int i=0;i<arr.length;i++){
System.out.print("   " + arr[i] );
}
//boolean
System.out.println("\nBoolean " + b1);
}
}
