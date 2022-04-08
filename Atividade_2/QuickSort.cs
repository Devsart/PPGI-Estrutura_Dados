using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_2
{
    public class QuickSort
    {
        public static long[] Sort(long[] lista, int pivoPos, int fim)
        {
            {
                if (pivoPos < fim)
                {
                    int pivo = Particao(lista, pivoPos, fim);
                    if (pivo > 1)
                    {
                        Sort(lista, pivoPos, pivo - 1);
                    }
                    if (pivo + 1 < fim)
                    {
                        Sort(lista, pivo + 1, fim);
                    }
                }
            }
            return lista;
        }
        public static int Particao(long[] lista, int m, int n)
        {
            long pivot = lista[m];
            while (true)
            {
                while (lista[m] < pivot)
                {
                    m++;
                }
                while (lista[n] > pivot)
                {
                    n--;
                }
                if (m < n)
                {
                    long temp = lista[m];
                    lista[m] = lista[n];
                    lista[n] = temp;
                    m++;
                    n--;
                }
                else
                {
                    return n;
                }
            }
        }
    }
}
