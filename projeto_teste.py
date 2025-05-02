import pandas as pd
import numpy as np
# se conctar com a planilha
conectar_dados = pd.read_excel("matches Manchester City.xlsx", sheet_name="Estatísticas")

def primeiro_tempo(): #tranformar isso em uma função para poder fazer isso com outros times tambem
    arr = np.array(conectar_dados) #tranformar os dados da planilha em uma array
    macara = arr == "1° Tempo" # a condição
    linhas_com_1tempo = np.any(macara, axis=1) # onde está cada uma das linhas que tem essa condição no eixo 1
    linha_filtrada = arr[linhas_com_1tempo] # filtro já funcionando
    print(linha_filtrada) # mostrar o que foi feito


def segundo_tempo():
    arr = np.array(conectar_dados)
    mascara = arr == "2° Tempo"
    linhas_com_2tempo = np.any(mascara, axis=1)
    filtro = arr[linhas_com_2tempo]
    print(filtro)

def integral():
    arr = np.array(conectar_dados)
    mascara = arr == "Integral"
    linhas = np.any(mascara, axis=1)
    filtro = arr[linhas]
    print(filtro)

primeiro_tempo() # chamar a função
print("-=" * 60)
segundo_tempo()
print("-=" * 60)
integral()