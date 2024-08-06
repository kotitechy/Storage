using System;
using System.Collections.Generic;
using System.Text;
using System.linq;
namespace Program
    class LeapYear{
    public static void main(String args[]){
        LeapYear lp = new LeapYear();
        lp.readdata();
        lp.leap();
        
    }
    int y;
    public void readdata(){
        Console.WriteLine("Enter an Yeart to find out wheather year is leap year or not : ")
        y = Convert.ToInt32(Console.ReadLine());
    }
    public void leap(){
        if ((y % 4 == 0 && (y % 100 != 0)|| (y% 400==0)))
        {
            Console.WriteLine("{0}")
        }
    }
}