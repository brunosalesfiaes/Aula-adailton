## principais bilbiotecas para o curso 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Aluguel.csv')  

df.head()
df.info()
df.describe().round(1) 
##def encontrar_maior_valor(df, coluna=None):

##correleclao = df ['Valor'].corr(df['Condominio'])
##print(f'correleção Valor x Condominio: {correleclao:.2f}')
##plt.bar(Tipo, Valor, color='red')
plt.figure(figsize=(8, 5))
##plt.scatter(df['chuva_mm'], df['produtividade_sc_ha'], alpha=0.6)
plt.xlabel('Valor')
plt.ylabel('IPTU')
plt.title('Relação de Valor e IPTU do imovel ')
plt.show()

