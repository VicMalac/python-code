class Program
{
    static void Main(string[] args)
    {
        // Vetor para armazenar as 4 notas
        double[] notas = new double[4];
        double soma = 0;

        // Estrutura de repetição para ler as notas
        for (int i = 0; i < 4; i++)
        {
            Console.Write($"Digite a nota {i + 1}: ");
            notas[i] = Convert.ToDouble(Console.ReadLine());
            soma += notas[i]; // Soma as notas
        }

        // Chamada da função para calcular a média
        double media = CalcularMedia(soma, notas.Length);

        // Estrutura de decisão para verificar aprovação
        if (media >= 7.0)
        {
            Console.WriteLine($"Média: {media:F1} - Aluno aprovado!");
        }
        else if (media >= 5.0 && media < 7)
        {
            Console.WriteLine($"Média: {media:F1} - Aluno em recuperação.");
        }
        else
        {
            Console.WriteLine($"Média: {media:F1} - Aluno reprovado.");
        }
    }

    // Função que calcula a média
    static double CalcularMedia(double total, int quantidade)
    {
        return total / quantidade;
    }
}