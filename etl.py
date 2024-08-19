import csv
from typing import Dict, List
# Ler CSV
# Output: Transformar em lista de dicionários com dados
def ler_csv(nome_do_arquivo :str) -> list[dict]:
   """
   Função que lê um arquivo CSV e retorna uma lista de dicionários, contendo as linhas e valores do arquivo.
   """ 
   with open (nome_do_arquivo, mode="r", encoding="utf-8") as arquivo:
        lista_dic_vals_csv = []
        dict_reader_obj = csv.DictReader(arquivo)
        for linha in dict_reader_obj:
            lista_dic_vals_csv.append(linha)
   
   return list(lista_dic_vals_csv)

def processar_lista(lista_de_dicionarios :List[dict], chave_promovida :str) -> Dict:
    
    """
    Função que recebe uma lista de dicionários e retorna outra lista de dicionários, com os valores de uma das chaves da lista de entrada como chaves dos novos dicionários. 
    """
    
    dict_processado: Dict[str,List[Dict]]= {}
    
    for dicionario in lista_de_dicionarios:
                
        valor_chave_promovida = dicionario[chave_promovida]
        dicionario_restante = {k:v for k,v in dicionario.items() if k != chave_promovida}

        if valor_chave_promovida not in dict_processado:
            dict_processado[valor_chave_promovida] = []

        dict_processado[valor_chave_promovida].append(dicionario_restante)

    return dict_processado

def vendas_agregadas(dicionario_processado: Dict) -> Dict:

    total_vendas_agregado: Dict[str, int] = {}

   # for k,v in dicionario_processado.items()

    for k,v in dicionario_processado.items():
        if k not in total_vendas_agregado:
            total_vendas_agregado[k] = 0
    
        for i in v:
            total_vendas_agregado[k] += int(i["Quantidade"]) * int(i["Venda"])

    return total_vendas_agregado



