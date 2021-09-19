# Assignment de Teste Funcional

Neste _assignment_ o estudante deve gerar casos de teste empregando os critérios de Particionamento em Classes de Equivalência e Grafo de Causa e Efeito.

## Particionamento em Classes de Equivalência

Para cada uma das especificações apresentadas abaixo, apresente as classes de equivalência e os casos de teste para situações válidas e inválidas. É fundamental explicitar quais são os casos de teste gerados para cada classe de equivalência. Além disso, para cada caso de teste de uma situação válida, deve-se explicitar as entradas e saídas esperadas.

1. Dada uma sequência de n números inteiros fornecidos, é necessário determinar um segmento de soma máxima. Exemplo: Na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1, o segmento de soma máxima é 3, 14, 10, -3, 9 e a soma do segmento é 33. É necessário criar um método para resolver esse tipo de problema. O método deve: se chamar somaMaxima; receber como parâmetro um vetor de inteiros vetor; retornar um valor inteiro que é a soma do segmento de soma máxima.

1. Um número perfeito é um número inteiro cuja soma de seus divisores (excluído o próprio número) coincide com o número. Esse é o caso, por exemplo, do número 28, em que os números 1, 2, 4, 7 e 14 são seus divisores e a soma desses divisores dá 28. Faça um método que verifica se um número é perfeito ou não. O método deve: se chamar numeroPerfeito; receber como parâmetro um valor inteiro num; retornar um valor booleano que é True, quando o número é perfeito e, um valor booleano False, quando o número não é perfeito.

1. É necessário calcular a média dos valores que estão na interseção entre dois conjuntos. Tem-se dois vetores de tamanho m e n, respectivamente.  Dados os vetores, deve-se verificar os valores presentes nos dois vetores (a interseção) e calcular a média aritmética desses valores que estão na interseção. Por exemplo, se vetor1=[19, 5, 2, 6] e vetor2=[5, 0, 9, 4, 18, 56], o valor resultante deve ser 5. Outro exemplo, se vetor1=[1, 3, 2, 6] e vetor2=[7, 0, 9, 4, 3, 1], o valor resultante deve ser 2. Nesse caso, já está validado que cada vetor é um conjunto, ou seja, ele não possui valores repetidos. O método deve: se chamar mediaIntersecao; receber como parâmetro m e n, vetor1 e vetor2; retornar o valor float que é da média dos valores na interseção entre os dois conjuntos; retornar o valor 0 se não houver interseção.

1. Em um dado domínio de negócio, um identificador (id) para ser considerado válido deve: 1) começar com uma letra; 2) conter apenas letras ou dígitos; 3) ter no mínimo 1 caractere e no máximo 6 caracteres de comprimento. Exemplo: "abc12" é válido; "cont\*1" é inválido; "1soma" é inválido; e, "a123456" é inválido. Faça um método que verifica se um identificador é válido ou inválido. O método deve:  se chamar validaID; receber como parâmetro uma sequência de caracteres é que o identificador id; retornar um valor booleano que é True, quando o identificador é válido e, retornar um valor booleano é False, quando o identificador é inválido. 

## Grafo de Causa e Efeito

Considerando a especificação, o estudante deve: 1) Identificar as causas e os efeitos; 2) apresentar o grafo de causa e feito - deve ser apenas um grafo, é proibido dividi-lo em vários; 3) apresentar a tabela verdade - deve ser apenas uma tabela, é proibido dividi-la em várias; 4) apresentar os casos de teste - com entrada e saída esperada - para situações válidas, que foram derivados do grafo de causa e feito e da tabela verdade. Atenção: precisa ser o grafo baseado em valores e operadores lógicos e com o emprego de restrições, árvores de decisão não serão aceitas.

1. É preciso saber o estado do aluno  a partir dos seus dados de frequência e nota. A especificação diz: O aluno pode estar "reprovado", "aprovado" ou "em recuperação". Se ele tem nota inferior a 40 ou se tiver frequência inferior a 20 aulas, ele está reprovado. Se ele tem nota igual ou superior a 60 e se não tiver frequência inferior a 20 aulas, ele está aprovado. Se ele tem nota maior ou igual a 40 e menor que 60 e também se não tiver frequência inferior a 20 aulas, ele está em recuperação.

1. É preciso saber o estado do participante a partir dos seus dados de número de denúncias e quantidade de reincidência em uma mesma violação. A especificação diz “O participante pode estar "banido", "ativo" ou "em observação". Se foi denunciado uma quantidade de vezes maior que  20 ou se tiver uma quantidade de reincidência em uma mesma violação maior ou igual a 5, ele está banido. Se foi denunciado uma quantidade de vezes menor que 10 e se tiver uma quantidade de reincidência em uma mesma violação menor que 5 , ele está ativo Se ele foi denunciado uma quantidade de vezes maior ou igual a 10 e menor ou igual a 20 e se tiver uma quantidade de reincidência em uma mesma violação menor que 5, ele está em observação.”

1. É preciso saber o nível de risco  a partir dos dados de temperatura e pressão. A especificação diz “O risco pode ser "alto", "médio" ou "baixo". Se a temperatura é maior ou igual a 50 ou se a pressão é superior a 50, o risco é alto. Se a temperatura é superior a 10 e inferior a 30 e a pressão é inferior a 20, o risco é baixo. Se a temperatura for maior ou igual a 30 e menor que 50 e se a pressão não for superior a 50, o risco é médio.”