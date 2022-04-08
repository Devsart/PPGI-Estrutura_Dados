using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atividade_2
{
    public class MergeSort
    {
        public static void Merge(long[] lista, int inicio,int meio, int fim)
        {
            long[] esquerda = new long[meio - inicio + 1];
            long[] direita = new long[fim - meio];
            Array.Copy(lista, inicio, esquerda, 0, meio - inicio + 1);
            Array.Copy(lista, meio + 1, direita, 0, fim - meio);
            int i = 0;
            int j = 0;
            for (int k = inicio; k < fim + 1; k++)
            {
                if (i == esquerda.Length)
                {
                    lista[k] = direita[j];
                    j++;
                }
                else if (j == direita.Length)
                {
                    lista[k] = esquerda[i];
                    i++;
                }
                else if (esquerda[i] <= direita[j])
                {
                    lista[k] = esquerda[i];
                    i++;
                }
                else
                {
                    lista[k] = direita[j];
                    j++;
                }
            }
        }
        public static long[] Sort(long[] lista, int inicio, int fim)
        {
            if (inicio < fim)
            {
                int meio = (inicio + fim) / 2;
                Sort(lista, inicio, meio);
                Sort(lista, meio + 1, fim);
                Merge(lista, inicio, meio, fim);
            }
            return lista;
        }
    }
}
