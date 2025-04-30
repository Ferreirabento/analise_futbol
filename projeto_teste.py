import pandas as pd
import numpy as np
# se conctar com a planilha
conectar_dados = pd.read_excel("matches Manchester City.xlsx", sheet_name="Estatísticas")

#coletar os dados
dados = np.array(conectar_dados)

#dados do primeiro tempo
primeiro_tempo = np.array(dados[1:46])


#limpar os dados

#analisar os dados
#media dos ultimos 5  jogos
#media dos 3 ultimos jogos
# processar os dados

#visualização dos dados (opcional)