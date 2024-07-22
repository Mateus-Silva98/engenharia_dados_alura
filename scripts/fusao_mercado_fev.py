from processamento_dados import Dados
import os

# Função para verificar se o arquivo existe
def verifica_arquivo(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

# Caminhos dos arquivos
path_json = os.path.abspath('../data_raw/dados_empresaA.json')
path_csv = os.path.abspath('../data_raw/dados_empresaB.csv')

# Verifica se os arquivos existem
verifica_arquivo(path_json)
verifica_arquivo(path_csv)

print('teste')

# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

# Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

# Load
path_dados_combinados = os.path.abspath('../data_processed/dados_combinados.csv')
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)
