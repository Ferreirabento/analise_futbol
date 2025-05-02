import pandas as pd
import numpy as np
# se conctar com a planilha
conectar_dados = pd.read_excel("matches Manchester City.xlsx", sheet_name="Estatísticas")

def primeiro_tempo(): #tranformar isso em uma função para poder fazer isso com outros times tambem
    arr = np.array(conectar_dados) #tranformar os dados da planilha em uma array
    macara = arr == "1° Tempo" # a condição
    linhas_com_1tempo = np.any(macara, axis=1) # onde está cada uma das linhas que tem essa condição no eixo 1
    linha_filtrada = arr[linhas_com_1tempo] # filtro já funcionando
    return linha_filtrada # mostrar o que foi feito


def segundo_tempo():
    arr = np.array(conectar_dados)
    mascara = arr == "2° Tempo"
    linhas_com_2tempo = np.any(mascara, axis=1)
    filtro = np.array(arr[linhas_com_2tempo])
    return filtro

def integral():
    arr = np.array(conectar_dados)
    mascara = arr == "Integral"
    linhas = np.any(mascara, axis=1)
    filtro = np.array(arr[linhas])
    return filtro

def gols(tempo_array):
    array = np.array(tempo_array)
    marcara_gols = array == "Gols"
    busca = np.any(marcara_gols, axis=1)
    filtro = array[busca]
    return filtro

def finalizacoes(tempo_array):
    arr = np.array(tempo_array)
    marcara = arr == "Finalizações"
    busca = np.any(marcara, axis=1)
    filtro = arr[busca]
    return filtro

def chute_ao_gol(tempo_array):
    arr = np.array(tempo_array)
    mascara = arr == "Chutes ao Gol"
    busca = np.any(mascara, axis=1)
    filtro = arr[busca]
    return filtro

def escanteios(tempo_array):
    arr = np.array(tempo_array)
    mascara = arr == "Escanteios"
    busca = np.any(mascara, axis=1)
    filtro = arr[busca]
    return filtro

def cartao_amarelo(tempo_array):
    arr = np.array(tempo_array)
    mascara = arr == "Cartões Amarelo"
    busca = np.any(mascara, axis=1)
    filtro = arr[busca]
    print(filtro)


