
from etl import ler_csv, processar_lista, vendas_agregadas

path_arquivo_csv = "vendas.csv"

vendas_itens :list[dict]

vendas_itens = ler_csv(path_arquivo_csv)

print(vendas_itens)

print("----")

chave_agrupadora = "Categoria"

vendas_agregadas_categoria = processar_lista(vendas_itens,chave_agrupadora)

print(vendas_agregadas_categoria)

print("----")

total_vendas = vendas_agregadas(vendas_agregadas_categoria)

print(total_vendas)
