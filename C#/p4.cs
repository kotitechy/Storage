//taking user input String , number

using System;

class p4{
static void Main(String[] args){
//String input
Console.WriteLine("Enter your name : ");
String name = Console.ReadLine();

//int input
Console.WriteLine("Enter Your Age : ");
int age = Convert.ToInt32(Console.ReadLine());

Console.WriteLine("Student Deatils are : \n name : " + name + " \n age : " + age );
}
}