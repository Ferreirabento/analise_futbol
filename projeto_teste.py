import pandas as pd
import numpy as np
# se conctar com a planilha
conectar_dados = pd.read_excel("matches Manchester City.xlsx", sheet_name="Estatísticas")

def primeiro_tempo():
    arr = np.array(conectar_dados)
    macara = arr == "1° Tempo"
    linhas_com_1tempo = np.any(macara, axis=1)
    linha_filtrada = arr[linhas_com_1tempo]
    print(linha_filtrada)

primeiro_tempo()