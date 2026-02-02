import pandas as pd
import numpy as np

try:
    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    df_estel = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='ISO-8859-1')

    df_estelionato = df_estel[['munic', 'estelionato', 'mes']]

    df_estelionato_ordenado = df_estelionato.groupby(['munic'])['estelionato'].sum().reset_index()

    print(df_estelionato_ordenado.head())
except Exception as e:
    print(f"Erro ao carregar os dados: {e}")

# Identificando padrão de estelionato em municípios
try:
    print('Obtendo informações do padrão de estelionato')

    array_estelionato = np.array(df_estelionato_ordenado['estelionato'])

    # medidads de tendência central
    media = np.mean(array_estelionato)
    mediana = np.median(array_estelionato)
    distancia_media_mediana = (media - mediana) / mediana


    print(f'\nMédia: {media:.3f}')
    print(f'Mediana: {mediana}')
    print(f'Distância Média e Mediana: {distancia_media_mediana:.3f}')

except Exception as e:
    print(f'Erro ao obter informações... {e}')
