🧠 Desafio: Simulador de Apostas
🎯 Objetivo
Criar um simulador simples de apostas onde o jogador tenta adivinhar o número sorteado em um jogo de dados, com base em suas apostas.

🎲 Funcionalidades
Escolha do valor da aposta
O jogador escolhe quanto quer apostar, com um valor inicial de 100.

Escolha do número
O jogador escolhe um número de 1 a 6, tentando adivinhar o número que será sorteado (simulando o lançamento de um dado).

Sortear número
O programa simula o lançamento de um dado, gerando um número aleatório de 1 a 6.

Resultado da aposta
Se o jogador adivinhar o número sorteado, ele ganha o valor da aposta multiplicado por 2. Caso contrário, ele perde o valor da aposta.

Exibição do saldo
Após cada rodada, o programa exibe o saldo atual do jogador.

Finalização do jogo
O jogo continua até que o saldo do jogador chegue a 0.

🧱 Estrutura inicial
Saldo do jogador: Começa com 100

Opções de escolha: O jogador escolhe o valor da aposta e o número que deseja apostar (de 1 a 6).

Sorteio: Usar random.randint(1, 6) para gerar o número sorteado.

Resultado: Exibir o resultado da rodada (se acertou ou errou).

💡 Extras opcionais
Limitar o número de apostas: O jogador só pode fazer um número limitado de apostas (ex: 5 rodadas).

Adicionar um jackpot: Se o jogador apostar no número exato e acerto em 3 rodadas consecutivas, ganha o jackpot (ex: 5x o valor apostado).