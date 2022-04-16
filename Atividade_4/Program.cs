using System;
using System.Diagnostics;
using System.IO;

namespace Atividade_4
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
                mString = "maxHeapify";
                sw.Start();
                listaOrd = MaxHeap.Sort(listaNum);
                sw.Stop();
            }
            else if (metodo == "2")
            {
                mString = "heapSort";
                sw.Start();
                listaOrd = HeapSort.Sort(listaNum);
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
            Console.WriteLine("\n\nEstas sao opcoes para o metodo de ordenacao:\n\n1 - Heap Maximo\n2 - Heap Sort\n\nEscolha um dos valores:");
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
    }
}
