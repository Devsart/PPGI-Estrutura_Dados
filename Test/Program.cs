using System;
using System.Linq;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            long[] b = { 321313, 3232, 32, 54, 55,932,1,2,5,88,76576 };
            var max = b.Max();
            var exp = 10;
            Console.WriteLine(b);
            Console.ReadKey();
        }
    }
}
