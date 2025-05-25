# Simulador-de-Entrada-de-Imovel
Feito por Felipe Frug

## Como funciona
De forma a rodar o codigo é necessário alterar apenas as variaveis abaixo no arquivo main.py para o valor desejado:

- `valor_do_imovel`
- `entrada`
- `tempo_contrato`
- `taxa_juros`

para instalar as bibliotecas necessárias utilize o comando abaixo:

pip install -r requirements.txt

## Escolhas feitas
As funções utilizadas foram feitas em outro arquivo para que seja mais facil de entender e eventualmente alterar o código.

O calculo do valor de entrada, total a guardar e parcela mensal foram feitos diretamente no main por serem muito simples

O calculo do valor das parcelas para cada ano de contrato, tanto pelo igpm quanto pelo juros anual foram feitos em funções separadas para que seja mais facil de entender e eventualmente alterar o código.

Caso desejado é possivel passar o valor do igpm para a função main, mas o codigo usa 6% como padrão.

A simulação é feita pelo terminal e através de um gráfico demonstrando quanto será o valor de uma parcela mensal por igpm e quanto será o valor pelos juros compostos.

O gráfico foi feito de forma a facilitar a comparação entre os dois valores.