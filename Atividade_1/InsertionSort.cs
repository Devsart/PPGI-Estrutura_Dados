using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_1
{
    public class InsertionSort
    {
        public static long[] Sort(long[] lista)
        {
            for (int i = 1; i < lista.Length; i++)
            {
                long aux = lista[i];
                int j = i - 1;

                while (j >= 0 && lista[j] > aux)
                {
                    lista[j + 1] = lista[j];
                    j -= 1;
                }
                lista[j + 1] = aux;
            }
            return lista;
        }
    }
    
}
