from functions import parcela_mensal_juros, parcela_mensal_igpm

# As unicas coisas que devem ser alteradas de forma a fazer o programa funcionar são as quatro variaveis abaixo
valor_do_imovel = 500000
entrada = 5
tempo_contrato = 3
taxa_juros = 8

def main(valor_do_imovel: float, entrada: float, tempo_contrato: int, taxa_juros: float, igmp: float = 6):
    valor_entrada = valor_do_imovel * (entrada / 100) # calculo de valor da entrada conforme referencia
    total_a_guardar = valor_do_imovel * 0.15 # calculo do total a guardar conforme referencia
    parcela_mensal = total_a_guardar / (tempo_contrato*12) # calculo da parcela mensal conforme referencia

    lista_valor_juros = parcela_mensal_juros(parcela_mensal, tempo_contrato, taxa_juros)
    lista_valor_igpm = parcela_mensal_igpm(parcela_mensal, tempo_contrato, igmp)
    print(f"Valor de entrada: {valor_entrada:.2f}")
    print(f"Valor a guardar: {total_a_guardar:.2f}")
    print(f"Valor mensal base: {parcela_mensal:.2f}")
    print(f"valor mensal pelo igpm:")

    for indice in range(len(lista_valor_igpm)):
        print(f"Ano {indice}: R$ {lista_valor_igpm[indice]:.2f}", )

    if taxa_juros < 5 and taxa_juros > 12:
        print("Taxa de juros não está no intervalo indicado, por favor verifique a taxa de juros")
        return
    
    print(f"valor mensal com {taxa_juros}% ao ano:")
    for indice in range(len(lista_valor_juros)):
        print(f"Ano {indice}: R$ {lista_valor_juros[indice]:.2f}", )
    return


main(valor_do_imovel,entrada,tempo_contrato,taxa_juros) # chama a funcao main para executar o programa