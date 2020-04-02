# Assignment  3

## Atividade de Teste Estrutural

Neste _assignment_ o estudante deve exercitar seus conhecimentos de teste estrutural. Para isso ele deve:
1. Em uma mesma classe, implementar dois métodos que solucionam problemas computacionais
1. Derivar o Grafo de Fluxo de Controle de cada método
1. Determinar a complexidade ciclomática de cada grafo 
1. Determinar um conjunto base de caminhos linearmente independentes a partir de cada grafo e do valor de complexidade ciclomática
1. Definir os casos de teste que vão forçar a execução de cada caminho do conjunto, indicando as entradas e respectivas saídas esperadas.
1. Implementar e executar uma suíte de testes, que contempla os casos de teste identificados

* Para realizar a entrega, o estudante deve usar o repositório criado para o _assignment 1_, o repositório tem prefixo _assignment1n_. Nesse repositório, o estudante deve criar uma pasta chamada *TesteEstrutural*. Dentro dessa pasta, o estudante deve colocar duas coisas: 1) um arquivo _markdown_ no qual deve apresentar os artefatos gerados (grafo, cálculos, caminhos, casos de teste) e 2) uma pasta chamada *codigo* que deve conter todos os códigos implementados (solução do problema computacional e suíte de testes).

* **Quais são os dois problemas computacionais que devo usar e para os quais eu devo implementar a solução?** Resposta: Você implementará a solução para dois dos quatro problemas apresentados na lista abaixo. Se o último número da sua matricula for par (ou zero), você usará no _assignment_ os problemas de número 1 e 2. Se o último número da sua matricula for impar, você usará no  _assignment_ os problemas de número 3 e 4. 

* **Qual linguagem de programação devo usar?** Resposta: A linguagem de programação que você desejar. Recomendo que você use a linguagem Python. Criei um [exemplo simples](https://github.com/TS-puc-20201/Teste-De-Software/tree/master/01-SlidesDasAulas/TS-06-C%C3%B3digo) de como fazer em Python. Para esse exemplo, usei um dos problemas que resolvemos na aula de Teste Estrutural.


## Lista de Problemas

1. Dada uma sequência de _n_ números inteiros fornecidos, é necessário determinar um segmento de soma máxima. Exemplo: Na sequência _5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1_, o segmento de soma máxima é _3, 14, 10, -3, 9_ e a soma do segmento é 33. É necessário criar um método para resolver esse tipo de problema. O método deve: 
	* se chamar _somaMaxima_
	* receber como parâmetro um vetor de inteiros _vetor_
	* retornar um valor inteiro que é a soma do segmento de soma máxima 

1. Um número perfeito é um número inteiro cuja soma de seus divisores (excluído o próprio número) coincide com o número. Esse é o caso, por exemplo, do número 28, em que os números _1, 2, 4, 7 e 14_ são seus divisores e a soma desses divisores dá 28. Faça um método que verifica se um número é perfeito ou não. O método deve:
	* se chamar _numeroPerfeito_
	* receber como parâmetro um valor inteiro _num_
	* retornar um valor booleano que é _True_, quando o número é perfeito e, um valor booleano _False_, quando o número não é perfeito

1. É necessário calcular a média dos valores que estão na interseção entre dois conjuntos. Tem-se dois vetores de tamanho _m_ e _n_, respectivamente.  Dados os vetores, deve-se verificar os valores presentes nos dois vetores (a interseção) e calcular a média aritmética desses valores que estão na interseção. Por exemplo, se _vetor1=[19, 5, 2, 6]_ e _vetor2=[5, 0, 9, 4, 18, 56]_, o valor resultante deve ser 5. Outro exemplo, se _vetor1=[1, 3, 2, 6]_ e _vetor2=[7, 0, 9, 4, 3, 1]_, o valor resultante deve ser 2. Nesse caso, já está validado que cada vetor é um conjunto, ou seja, ele não possui valores repetidos. O método deve:
	* se chamar _mediaIntersecao_
	* receber como parâmetro _m_ e _n_, _vetor1_ e _vetor2_
	* retornar o valor _float_ que é da média dos valores na interseção entre os dois conjuntos
	* retornar o valor 0 se não houver interseção

1. Em um dado domínio de negócio, um identificador (id) para ser considero válido deve: 1) começar com uma letra; 2) conter apenas letras ou dígitos; 3) ter no mínimo 1 caractere e no máximo 6 caracteres de comprimento. Exemplo: "abc12" é válido; "cont\*1" é inválido; "1soma" é inválido; e, "a123456" é inválido. Faça um método que verifica se um identificador é válido ou inválido. O método deve:
	* se chamar _validaID_
	* receber como parâmetro uma sequência de caracteres é que o identificador _id_
	* retornar um valor booleano que é _True_, quando o identificador é válido e, retornar um valor booleano é _False_, quando o identificador é inválido

---

_Lesandro Ponciano (lesandrop at pucminas) - PUC Minas_