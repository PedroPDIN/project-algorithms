# Boas-vindas ao repositório do projeto `Algorithms`!


<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Neste projeto tem como foco resolver problemas e otimizar algoritmos desenvolvendo a capacidade de implementar soluções para os mais diversos problemas do dia a dia!
  
  🚵 Habilidades exercitadas:
  
  Lógica;

  Capacidade de interpretação de problemas;

  Capacidade de interpretação de um código legado;

  Capacidade de otimizar a resolução de problemas e;

  Resolver problemas/Otimizar algoritmos sob pressão.
</details>

<details>
  <summary><strong>Instalação do projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-016-a-project-algorithms.git`.
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-016-a-project-algorithms`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
</details>

# Requisitos

## 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)

Você trabalha na maior empresa de educação do Brasil. Certo dia, a pessoa Product Manager `(PM)` quer saber qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma. Com esse dado em mãos, a pessoa PM saberá qual é o melhor horário para disponibilizar os materiais de estudo para ter o maior engajamento possível.

O horário de entrada e saída do sistema é cadastrado no banco de dados toda vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão contidos em uma lista de tuplas (`permanence_period`) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.

Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos de estudo. Para isso, utilize a estratégia de resolução de problemas chamada `força bruta` em que a função desenvolvida por você será chamada várias vezes com valores diferentes para a variável `target_time` e serão analisados os retornos da função.

:eyes: _De olho na Dica:_ O melhor horário será aquele no qual o contador retornado pela função for o maior

<details>
 <summary>
   <b>Clique aqui para ver um exemplo.</b>
 </summary>

```md
# Nos arrays temos 6 estudantes

# estudante             1       2       3       4       5       6
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa estudante ainda estavam estudando nesse horário.
target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante começaram a estudar nesse horário e a quarta ainda estava estudando.
target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante ainda estavam estudando nesse horário.
target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a quarta pessoa estudante estavam estudando nesse horário.
target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante estavam estudando nesse horário.

Para esse exemplo, depois de rodar a função para todos esses `target_times`, julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4 estudantes estavam presentes nesse horário!
```

</details>

- Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
  - O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução.

- O algoritmo deve utilizar a solução iterativa;

- Caso o `target_time` passado seja nulo, o valor retornado pela função deve ser `None` (considere o horário 0 como um horário válido);

- O código deve ser feito dentro do arquivo `challenges/challenge_study_schedule.py`.

## 2 - Palíndromos (Recursividade)

Escreva uma função que irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um _booleano_, `True` ou `False`.

Mas o que é um palíndromo?

> Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, `"ABCBA"`. 

<details>
 <summary>
   <b>Clique aqui para ver um exemplo.</b>
 </summary>

```md
word = "ANA"
# saída: True

word = "SOCOS"
# saída: True

word = "REVIVER"
# saída: True

word = "COXINHA"
# saída: False

word = "AGUA"
# saída: False
```

</details>

- O algoritmo deve ser feito utilizando a solução recursiva;

- Se for passado uma _string_ vazia, retorne `False`;

- O código deve ser feito dentro do arquivo `challenges/challenge_palindromes_recursive.py`.

## 3 - Anagramas (Algoritmo de ordenação)

Faça um algoritmo que consiga comparar duas _strings_ e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será um _booleano_, `True` ou `False`.

O algoritmo deve considerar letras _maiúsculas_ e _minúsculas_ como iguais durante a comparação das entradas, ou seja, ser _case insensitive_. 

Mas o que é um anagrama?

> "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."

<details>
 <summary>
   <b>Clique aqui para ver um exemplo.</b>
 </summary>

```md
first_string = "amor"
second_string = "roma"
# saída: True
# Explicação: Nesse caso o retorno da função é True, pois a palavra "roma" é um anagrama de "amor".


first_string = "pedra"
second_string = "perda"
# saída: True
# Explicação: Nesse caso o retorno também é True. Na palavra "pedra", trocamos o "d" de lugar com o "r" e formamos "perda", sendo assim um anagrama.  


first_string = "pato"
second_string = "tapo"
# saída: True


first_string = "Amor"
second_string = "Roma"
# saída: True
# Explicação: Nesse caso o retorno da função é True, pois a palavra "Roma" é um anagrama de "Amor" independente da letra "R" e "A" serem maiúsculas.


# Agora vamos pra um exemplo em que não existe um anagrama
first_string = "coxinha"
second_string = "empada"
# saída: False
```

</details>

- Este requisito será testado executando milhares de vezes sobre várias entradas com o tamanho variável. Tais execuções **no avaliador** irão determinar de maneira empírica, através de cálculos, a complexidade assintótica do seu algoritmo.
  - O tempo de execução do código na sua máquina pode variar em relação ao avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo de execução. Ainda assim, o que vale é o resultado do avaliador, e não o local. Na dúvida, busque ajuda do time de instrução;

- Utilize algoritmos de ordenação para realizar este requisito.
  - Utilize qualquer algoritmo que quiser (_Selection sort_, _Insertion sort_, _Bubble sort_, _Merge sort_, _Quick sort_ ou _TimSort_), desde que atinja a complexidade `O(n log n)`. 
  - :warning: Você deverá implementar **sua própria função de ordenação**, ou seja, o uso de funções prontas **não** é permitido.
    - Exemplos de funções não permitidas: _*sort*, *sorted* e *Counter*_;

- :warning: **Não** será permitido realizar nenhuma **importação** neste arquivo!

- A função retorna `True` caso uma _string_ **seja** um anagrama da outra independente se as letras são maiúsculas ou minúsculas;

- A função retorna `False` caso uma _string_ **não seja** um anagrama da outra;

- O código deve ser feito dentro do arquivo `challenges/challenge_anagrams.py`.

 #### :warning: Importante :warning:: O grupo Trybe foi responsável por realizar o inicio do projeto (e também os commits iniciais), mas precisamente a estrutura do projeto e as configuração dos tests para a avaliação do projeto.