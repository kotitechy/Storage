using System;

namespace access specifier
{
    class program 
    {
        two b=new two();
        b.show();
    }
    class one 
    {
        //private int x;
        protected int y;
        internal int z;
        public int a;
        protected internal int b;
    }
    class two : one 
    {
        public void show ()
        {
            console.writeline("values are :");
           // x=10;
            y=20;
            z=50;
            a=12;
            b=90;
            console.writeline(y);
          //  console.writeline(x);
            console.writeline(z);
            console.writeline(a);
            console.writeline(b);
            console.readline();
            }
            }
            }
