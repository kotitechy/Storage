using System;

namespace CheckLeapYear{
    class pg1{
        public static void main(String [] args){
            Console.Writeline("Enter van leap year: ");
            int y = int.Parse(Console.ReadLine());
            if (((y % 4 == 0) && (y % 100 != 0 ) ) || (y % 400 == 0 )){
            Console.Writeline("Year "+ y + " is an leap year");
            }
            else{
            Console.Writeline("Year is not an leap year: ");
            }
        }
    }
}