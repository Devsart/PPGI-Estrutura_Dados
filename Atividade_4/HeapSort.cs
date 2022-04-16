using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_4
{
    public class HeapSort
    {
        public static long[] Sort(long[] lista)
        {
            int n = lista.Length;
            for (int i = n / 2 - 1; i >= 0; i--)
                MaxHeap.Heapify(lista, n, i);
            for (int i = n - 1; i >= 0; i--)
            {
                MaxHeap.Swap(lista, i, 0);
                MaxHeap.Heapify(lista, i, 0);
            }
            return lista;
        }
    }
}
