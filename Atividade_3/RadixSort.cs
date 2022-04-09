using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_3
{
    public class RadixSort
    {
        public static void countSortSpecial(long[] lista, int n, int exp)
        {
            long[] output = new long[n];
            int i;
            int[] count = new int[10];

            for (i = 0; i < 10; i++)
                count[i] = 0;

            for (i = 0; i < n; i++)
                count[(lista[i] / exp) % 10]++;

            for (i = 1; i < 10; i++)
                count[i] += count[i - 1];

            for (i = n - 1; i >= 0; i--)
            {
                output[count[(lista[i] / exp) % 10] - 1] = lista[i];
                count[(lista[i] / exp) % 10]--;
            }

            for (i = 0; i < n; i++)
                lista[i] = output[i];
        }
        public static long[] Sort(long[] lista)
        {
            // Encontrando valor máximo
            int n = lista.Length;
            long max = 0;
            for (int i = 0; i < n; i++)
            {
                if (max < lista[i])
                {
                    max = lista[i];
                }
            }
            for (int exp = 1; max / exp > 0; exp *= 10)
                countSortSpecial(lista, n, exp);
            return lista;
        }
    }
}
