import numpy as np
import Filtros as fit

# media de escanteios no primeiro tempo jogando em casa
while True:
    tempo = int(input("""
======= Qual tempo deseja apostar ========:
         [ 1 ] primeiro tempo
         [ 2 ] segundo tempo
         [ 3 ] integral
         opção: """))
    if tempo == 1:
        tempo = fit.primeiro_tempo()
    elif tempo == 2:
        tempo = fit.segundo_tempo()
    elif tempo == 3:
        tempo = fit.integral()
    else:
        print("por favor escolhas uma das opçoes acima")
    categoria = int(input("""
======= Qual categoria deseja apostar ========:
         [ 1 ] gols 
         [ 2 ] finalizacoes
         [ 3 ] chute ao gol
         [ 4 ] escanteios
         [ 5 ] cartao amarelo
         opção: """))
    if categoria == 1:
        categoria = fit.gols(tempo)
    elif categoria == 2:
        categoria = fit.finalizacoes(tempo)
    elif categoria == 3:
        categoria = fit.chute_ao_gol(tempo)
    elif categoria == 4:
        categoria = fit.escanteios(tempo)
    elif categoria == 5:
        categoria = fit.cartao_amarelo(tempo)
    else:
        print("por favor escolhas uma das opçoes acima")

    
    
"""primeiro_tempo = fii.primeiro_tempo()

escanteios = fii.escanteios(primeiro_tempo)

convertidos = fii.convertidos_casa(escanteios)

media = fii.valores(convertidos)
"""