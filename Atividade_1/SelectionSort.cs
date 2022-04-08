using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_1
{
    public class SelectionSort
    {
        public static long[] Sort(long[] lista)
        {
            for(int i=0; i <= lista.Length - 1; i++)
            {
                int min = i;
                for (int j = (i + 1); j < lista.Length; j++)
                {
                    if (lista[j] < lista[min])
                    {
                        min = j;
                    }
                }
                if (lista[i] != lista[min])
                {
                    long aux = lista[i];
                    lista[i] = lista[min];
                    lista[min] = aux;
                }
            }
            return lista;
        }
    }
}
