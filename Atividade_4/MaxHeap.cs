using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_4
{
    public class MaxHeap
    {
        private static int GetLeftChildIndex(int elementIndex) => 2 * elementIndex + 1;
        private static int GetRightChildIndex(int elementIndex) => 2 * elementIndex + 2;
        private int GetParentIndex(int elementIndex) => (elementIndex - 1) / 2;
        public static void Swap(long[] lista,int firstIndex, int secondIndex)
        {
            var temp = lista[firstIndex];
            lista[firstIndex] = lista[secondIndex];
            lista[secondIndex] = temp;
        }
        public static void Heapify(long[] lista,int n, int i)
        {
            int imax = i;
            int ie = GetLeftChildIndex(i);
            int id = GetRightChildIndex(i);
            if (ie < n && lista[ie] > lista[imax])
            {
                imax = ie;
            }
            if (id < n && lista[id] > lista[imax])
            {
                imax = id;
            }
            if(imax != i)
            {
                Swap(lista,imax,i);
                Heapify(lista, n, imax);
            }
        }
        public static long[] Sort(long[] lista)
        {
            Heapify(lista, lista.Length, 0);
            return lista;
        }
    }
}
