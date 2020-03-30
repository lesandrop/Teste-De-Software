# Assignment  3

## Atividade de Teste Estrutural

Neste _assignment_ o estudante deve exercitar seus conhecimentos de teste estrutural. Para isso ele deve:
1. Em uma mesma classe, implementar dois métodos que solucionam problemas computacionais
1. Derivar o Grafo de Fluxo de Controle de cada método
1. Determinar a complexidade ciclomática de cada grafo 
1. Determinar um conjunto base de caminhos linearmente independentes a partir de cada grafo
1. Prepare os casos de teste que vão forçar a execução de cada caminho do conjunto
1. Implementar e executar uma suite de testes, que contempla os casos de teste identificados

* Para realizar a entrega, o estudante deve usar o repositório criado para o _assignment 1_, o repositório tem prefixo _assignment1n_. Nesse repositório, o estudante deve criar uma pasta chamada *TesteEstrutural*. Dentro dessa pasta, o estudante deve colocar duas coisas: 1) um arquivo _markdown_ no qual deve apresentar os artefatos gerados (grafo, cálculos, caminhos, casos de teste) e 2) uma pasta chamada *codigo* que deve conter todos os códigos implementados (solução do problema computacional e suite de testes).

* Quais são os dois problemas computacionais que devo implementar a solução? Resposta: Cocê implementará a solução para dois problemas da lista abaixo. Se o último número da sua matricula for par (ou zero), você fará os problemas 1  e 2. Se o último número da sua matricula for impar, você fará os problemas 2  e 4. 

* Qual linguagem de programação posso usar? Resposta: A que você desejar. Recomendo Python. Usando um dos problemas da aula de Teste Estrutural, criei um [exemplo simples](https://github.com/TS-puc-20201/Teste-De-Software/tree/master/01-SlidesDasAulas/TS-06-C%C3%B3digo) de como fazer em Python.


## Lista de Problemas

1. Dada uma sequência de n números inteiros fornecidos pelo usuário, determinar um segmento de soma máxima. Exemplo: Na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1, a soma do segmento é 33, pois o segmento de soma máxima é 3, 14, 10, -3, 9. O método deve: 
	* se chamar somaMaxima
	* receber como parâmetro um vetor de inteiros vetor
	* retornar um valor inteiro que é a soma do segmento de soma máxima 

1. Um método calcula a média dos valores que estão na interseção entre dois conjuntos. Dessa forma, o método recebe dois vetores de tamanho m e n, respectivamente.  Após isso, verificar os valores presentes nos dois vetores e calcular a média deles. Ex: se vetor1=[19, 5, 2, 6] e vetor2=[5, 0, 9, 4, 18, 56], deverá ser impresso o valor 5. De outro modo, se vetor1=[1, 3, 2, 6] e vetor2=[7, 0, 9, 4, 3, 1], deverá ser impresso o valor 2. Nesse caso, os vetores são conjuntos, ou não, eles não possuem valores iguais. O método deve:
	* se chamar mediaIntesercao
	* receber como parâmetro m e n, vetor1 e vetor2
	* retornar o valor float que é da média dos valores na interseção entre os dois conjuntos

1. Um número perfeito é um número inteiro cuja soma de seus divisores (excluído o próprio número) coincide com o número. Esse é o caso, por exemplo, do número 28, em que os números 1, 2, 4, 7 e 14 são seus divisores e a soma desses divisores dá 28. Faça um método que verifica se um número é perfeito ou não. O método deve:
	* se chamar numeroPerfeito
	* receber como parâmetro um valor inteiro num
	* retornar um valor booleano que é True, quando o número é perfeito e é False, quando o número não é perfeito

1. Em domínio de negócio, um identificador para ser considero válido deve: 1) começar com uma letra; 2) conter apenas letras ou dígitos; 3) ter no mínimo 1 caractere e no máximo 6 caracteres de comprimento. Exemplo: “abc12” (válido), “cont*1” (inválido), “1soma” (inválido) e “a123456” (inválido). Faça um método que verifica se um identificador é válido ou não. O método deve:
	* se chamar validaID
	* receber como parâmetro uma sequência de caracteres é que o identificador id
	* retornar um valor booleano que é True, quando o identificador é válido e é False, quando o identificador não é válido
	
---

_Lesandro Ponciano (lesandrop at pucminas) - PUC Minas_