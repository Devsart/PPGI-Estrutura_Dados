using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_3
{
    public class CountingSort
    {
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
            // Construindo array de frequência
            int[] arr_freq = new int[max+1];
            for ( int i = 0; i < lista.Length; i++ )
            {
                long val = lista[i];
                arr_freq[val] += 1;
            }
            // Ordenando a partir do array de frequência
            for (int i = 0, j = 0; i < arr_freq.Length; i++)
            {
                while (arr_freq[i] > 0)
                {
                    lista[j] = i;
                    j++;
                    arr_freq[i]--;
                }
            }
            return lista;
        }
    }
}
