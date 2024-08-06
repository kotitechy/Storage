using System;

namespace Accelration{
    class pgt2{
        public static void main(String [] args){
            Console.WriteLine("Enter initial velocity: ");
            double in_v = Convert.ToDouble(Console.ReadLine());
            
            Console.WriteLine("Enter final velocity: ");
            double f_v = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter Time Taken: ");
            double t_t = Convert.ToDouble(Console.ReadLine());

            double d_v = f_v - in_v;
            double acc = d_v / t_t;
            Console.WriteLine($"Acceleartion is : {acc} m/s^2");
            Console.ReadKey();

            


        }
    }
}