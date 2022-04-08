using System;
using System.Diagnostics;
using System.IO;

namespace Atividade_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("********************************************");
            Console.WriteLine("**** Bem-vindo ao ordenador de inteiros ****");
            Console.WriteLine("********************************************");
            string arquivo;
            if (args.Length > 1)
            {
                arquivo = args[1];
            }
            else
            {
                Console.WriteLine("\n\nPor favor, digite o caminho para o arquivo que deseja ordenar:");
                arquivo = Console.ReadLine();
            }
            string[] linhas = File.ReadAllLines(arquivo);
            long[] listaNum = Array.ConvertAll(linhas, long.Parse);
            string metodo = EscolherMetodo();
            var sw = new Stopwatch();
            long[] listaOrd = Array.Empty<long>();
            string mString = "";
            if (metodo == "1")
            {
                mString = "quickSort"; 
                sw.Start();
                listaOrd = QuickSort.Sort(listaNum,0,listaNum.Length-1);
                sw.Stop();
            }
            else if (metodo == "2")
            {
                mString = "mergeSort";
                sw.Start();
                listaOrd = MergeSort.Sort(listaNum, 0, listaNum.Length - 1);
                sw.Stop();
            }
            Console.WriteLine("\n\nTempo de execucao: {0} ms.", sw.ElapsedMilliseconds);
            string[] listaOrdStr = Array.ConvertAll(listaOrd, Convert.ToString);
            var nomeArquivo = new DirectoryInfo(arquivo).Name;
            string pasta = "output";
            string fullPath = pasta + "/" + mString + "-" + sw.ElapsedMilliseconds + "ms-" + nomeArquivo;
            if (!Directory.Exists(pasta))
            {
                Directory.CreateDirectory(pasta);
            }
            File.WriteAllLines(fullPath, listaOrdStr);
            Console.WriteLine("\n\nArquivo de lista ordenada criado com sucesso!\nVoce pode encontra-lo no caminho especificado para a lista.\nMuito obrigado! :)");
            Console.ReadLine();
        }

        static string EscolherMetodo()
        {
            Console.WriteLine("\n\nEstas sao opcoes para o metodo de ordenacao:\n\n1 - Quick Sort\n2 - Merge Sort\n\nEscolha um dos valores:");
            string metodo = Console.ReadLine();
            if (metodo == "1")
            {
                return metodo;
            }
            else if (metodo == "2")
            {
                return metodo;
            }
            else
            {
                return EscolherMetodo();
            }
        }
        static void VerificarLista(long[] lista)
        {
            int marker = 0;
            for (int i = 0; i <= lista.Length - 2; i++)
            {
                if (lista[i + 1] < lista[i])
                {
                    Console.WriteLine("A ordenacao contem erro na posicao {0}", i);
                    marker++;
                }
            }
            Console.WriteLine("A lista contém {0} erros.", marker);
        }
    }
}
