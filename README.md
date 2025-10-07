# Down to one - Trabalho 1 - Projeto e Otimização de Algoritmos

## Descrição do problema

Um programa de contagem regressiva pode efetuar as operações:
1. Decréscimo unitário 
2. Divisão por 2 se não houver resto
3. Divisão por 3 se não houver resto

Qual o menor número de operações para contagem regressiva de um número *n*?

## Abordagem

Intuitivamente, podemos optar por uma abordagem gulosa: se *n* for divisível por 3, aplicamos esta operação, pois é o passo mais largo que podemos dar. Se não for, mas for divisível por 2, aplicamos esta operação, pois é o segundo passo mais largo que podemos dar. Em último caso, aplicamos operação de decréscimo. Após cada operação, repetimos esse processo recursivamente. O código ```down_to_one_greedy.py``` pode ser utilizado para esta abordagem.

Esta abordagem, entretando, não garante o melhor resultado sempre. Podemos provar isso encontrando um caso onde isso não acontece, que é o caso *n* igual a 10. 

A abordagem gulosa dará as seguintes operações: \2 -1 \2 \2

Porém existe uma sequência com menos operações: -1 \3 \3

Desta forma, o próximo passo é aplicar um algoritmo de programação dinâmica, que é ideal para esse tipo de situação.

Para esta abordagem, serão feitas as seguintes validações:

1. Se *n* é divisível por 6
1. Se *n* é divisível por 3
1. Se *n* é divisível por 2

Se *n* é divisível por 6, significa que qualquer uma das três operações pode ser utilizada. Desta forma, temos que avaliar as três e achar a que requer o menor número de passos, e repetir o processo recursivamente.

Se *n* é divisível por 3, significa que podemos aplicar a operação \3 ou -1. Desta forma, temos que avaliar as duas e achar a que requer o menor número de passos, e repetir o processo recursivamente.

Se *n* é divisível por 2, significa que podemos aplicar a operação \2 ou -1. Desta forma, temos que avaliar as duas e achar a que requer o menor número de passos, e repetir o processo recursivamente.

Em outros casos, a operação -1 deve ser utilizada, e repetir o processo recursivamente.

Este algoritmo retorna sempre o menor número de passos, e pode ser testado com o código ```down_to_one_dp.py```.

Por testar um grande número de caminhos, o código se mostra lento. Ele pode ser otimizado com memoização, salvando resultados anteriores para uso futuro. O código ```down_to_one_dp_memo.py``` pode ser utilizado para esta abordagem.

Finalmente, podemos retirar a recursão e aplicar uma abordagem *bottom-up* utilizando um vetor. O código ```down_to_one_aux_vector.py``` pode ser utilizado para esta abordagem.

## Resultado

Todos os códigos estão funcionais, porém a funcionalidade de fornecer a sequência utilizada só está presente no código ```down_to_one_dp.py``` e no código ```down_to_one_aux_vector.py```. A memoização tornou a implementação mais complexa e esta não foi realizada a tempo.