
def parcela_mensal_juros(parcela_base: float ,tempo_contrato: int, taxa_juros: float): 
    """
    essa funcao calcula o valor das parcelas para cada ano de contrato usando juros
    (foi feito em função de forma a facilitar a compreensão de um leitor externo)
    """
    
    lista_valor_anual = []
    lista_valor_anual.append(parcela_base) # valor inicial é o valor pago no primeiro ano
    valor_atual = parcela_base # inicializa o valor atual
    for i in range(tempo_contrato-1): # para os anos restantes calcula o valor atualizado
        valor_atual = valor_atual + (valor_atual * taxa_juros / 100) # valor atual é o valor anterior mais os juros em cima do valor anterior
        lista_valor_anual.append(valor_atual)
        # alterei a forma de forma que ficasse um pouco menos matemática e mais programação para facilitar a compreensão
    return lista_valor_anual # retorna os 4 valores


def parcela_mensal_igpm(parcela_base: float ,tempo_contrato: int, igpm: float): 
    """
    essa funcao calcula o valor das parcelas para cada ano de contrato usando igpm
    (foi feito em função de forma a facilitar a compreensão de um leitor externo)
    """
    
    lista_valor_anual = []
    lista_valor_anual.append(parcela_base) # valor inicial é o valor pago no primeiro ano
    valor_atual = parcela_base # inicializa o valor atual
    for i in range(tempo_contrato-1): # para os anos restantes calcula o valor atualizado
        valor_atual = valor_atual + (valor_atual * igpm / 100) # valor atual é o valor anterior mais o IGPM em cima do valor anterior
        lista_valor_anual.append(valor_atual)
        # alterei a forma de forma que ficasse um pouco menos matemática e mais programação para facilitar a compreensão
    return lista_valor_anual # retorna os 4 valores