import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

try:
    print('Obtendos dados...')

    ENDEREÇO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    #encondingo= 'utf-8', 'iso-8859-1', 'latin1', 'cp1252'
    df_ocorrencias = pd.read_csv(ENDEREÇO_DADOS, sep=';', encoding='iso-8859-1')

    # Delimitando as variáveis
    df_roubo_veiculos = df_ocorrencias[['munic', 'roubo_veiculo']]
    
    # Agrupando e quantificando por municipios
    df_roubo_veiculos = df_roubo_veiculos.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculos.head())
    

except Exception as e:
    print(f'Erro ao obter dados {e}')


# Obter informações de padrão de roubo de veículos
try:
    print(85 * '--')
    print('\nObtendo informações do padrão de roubos de veículos:')
    array_roubo_veiculos = np.array(df_roubo_veiculos['roubo_veiculo'])

    # Medidas de tendência central
    media = np.mean(array_roubo_veiculos)
    mediana = np.median(array_roubo_veiculos)
    distancia_media_mediana = (media - mediana) / mediana

    print('\nMedidas de tendência central:')
    print(f'Média: {media:.2f}')
    print(f'Mediana: {mediana:.2f}')
    print(f'Distância Média Mediana: {distancia_media_mediana:.2f}')


except Exception as e:
    print(f'Erro ao obter informações... {e}')


# Obtendo medidas estatísticas
try:
    print('\nMedidas de Posição:')
    q1 = np.quantile(array_roubo_veiculos, .25)
    q2 = np.quantile(array_roubo_veiculos, .50)
    q3 = np.quantile(array_roubo_veiculos, .75)
    print(f'q1: {q1}')
    print(f'q2: {q2}')
    print(f'q3: {q3}')

    # Menores
    df_roubo_veiculos_menores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] < q1]

    # Maiores
    df_roubo_veiculos_maiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] > q3]

    print(85 * '--')
    print(f'\nMunicipios de menores ocorrências de roubos de veículos:')
    print(df_roubo_veiculos_menores.sort_values(by='roubo_veiculo'))
    print(85 * '--')
    print(f'\nMunicipios de maiores ocorrências de roubos de veículos:')
    print(df_roubo_veiculos_maiores.sort_values(by='roubo_veiculo', ascending=False))
    
    # Medidas de dispersão
    maximo = np.max(array_roubo_veiculos)
    minimo = np.min(array_roubo_veiculos)
    amplitude_total = maximo - minimo

    print(85 * '--')
    print('\nMedidas de Dispersão: ')
    print(f'Máximo: {maximo}')
    print(f'Mínimo: {minimo}')
    print(f'Amplitude Total: {amplitude_total}')

    # Intervalo Interquartil
    iqr = q3 - q1
    
    # Limite Inferior
    limite_inferior = q1 - (1.5 * iqr)

    # Limite Superior
    limite_superior = q3 + (1.5 * iqr)

    # Zona de Corte
    print(85 * '--')
    print(f'Intervalo Interquartil: {iqr}')
    print(f'Limite Inferior: {limite_inferior}')
    print(f'Limite Superior: {limite_superior}')

    # Outliers Inferiores:
    df_roubo_veiculos_outliers_inferiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] < limite_inferior]

    # Outliers Superiores:
    df_roubo_veiculos_outliers_superiores = df_roubo_veiculos[df_roubo_veiculos['roubo_veiculo'] > limite_superior]

    print(85 * '--')
    print('Outliers Inferiores: ')
    if len(df_roubo_veiculos_outliers_inferiores) == 0:
        print('Não há outliers inferiores!')
    else:
        print(df_roubo_veiculos_outliers_inferiores)

    print('\nOutliers Superiores: ')
    if len(df_roubo_veiculos_outliers_superiores) == 0:
        print('Não há outliers superiores!')
    else:
        print(df_roubo_veiculos_outliers_superiores.sort_values(by='roubo_veiculo', ascending=False))


except Exception as e:
    print(f'Erro ao obter medidas estatísticas... {e}')

try:
    # pip install matplotlib
    print('\nVisualizando dados...')
    plt.subplots(2, 2, figsize=(16, 7))
    plt.suptitle('Análise de Boxplot')

    plt.subplot(2, 2, 1)
    plt.boxplot(array_roubo_veiculos, vert=False, showfliers=False, showmeans=True)
    plt.title('Gráfico Boxplot')

    plt.subplot(2, 2, 2)
    plt.boxplot(array_roubo_veiculos, vert=False, showmeans=True)
    plt.title('Gráfico Boxplot')

    plt.subplot(2, 2, 3)

    plt.subplot(2, 2, 4)

    plt.show()

except Exception as e:
    print(f'Erro ao plotar o gráfico {e}')

