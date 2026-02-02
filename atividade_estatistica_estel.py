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


 # Obtendo medidas estatísticas
try:

    q1 = np.quantile(array_estelionato, .25)
    q2 = np.quantile(array_estelionato, .50)
    q3 = np.quantile(array_estelionato, .75)

    print('\nMedidas de Posição:')
    print(30*'=')
    print(f'Q1: {q1}')
    print(f'Q2: {q2}')
    print(f'Q3: {q3}')

    # menores
    df_estelionato_menores = df_estelionato_ordenado[df_estelionato_ordenado['estelionato'] < q1]
    # maiores
    df_estelionato_maiores = df_estelionato_ordenado[df_estelionato_ordenado['estelionato'] > q3]

    print('\nMenores')
    print(30*'=')
    print(df_estelionato_menores.sort_values(by='estelionato', ascending=True))
    
    print('\nMaiores')
    print(30*'=')
    print(df_estelionato_maiores.sort_values(by='estelionato', ascending=False))

    # Mdidas de Dispersão
    maximo = np.max(array_estelionato)
    minimo = np.min(array_estelionato)
    amplitude_total = maximo - minimo

    print('\nPrintando Medidas de Dispersão:')
    print(30*'=')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude_total}')


    # Intervalo interquartil
    iqr = q3 - q1
    

    # Limite Inferior
    limite_inferior = q1 - (1.5 * iqr)

    # Limite superior
    limite_superior = q3 + (1.5 * iqr)

    print('\nMedidas de Dispersão')
    print(30*'=')
    print(f'IQR: {iqr}')
    print(f'Limite Inferior {limite_inferior}')
    print(f'Limite Superior {limite_superior}')


    # Outliers Inferiores:
    df_estelionato_outliers_inferiores = df_estelionato_ordenado[df_estelionato_ordenado['estelionato'] < limite_inferior]

    # Outliers superiores:
    df_estelionato_outliers_superiores = df_estelionato_ordenado[df_estelionato_ordenado['estelionato'] > limite_superior]

    print('\nOutliers Inferiores:')
    if len(df_estelionato_outliers_inferiores) == 0:
        print('Não há outliers inferiores')
    else:
        print(df_estelionato_outliers_inferiores.sort_values(by='estelionato', ascending=True))


    print('\nOutliers Superiores:')
    if len(df_estelionato_outliers_superiores) == 0:
        print('Não há outliers superiores')
    else:
        print(df_estelionato_outliers_superiores.sort_values(by='estelionato', ascending=False))
    

except Exception as e:
    print(f'Erro ao obter medidas estatísticas {e}')