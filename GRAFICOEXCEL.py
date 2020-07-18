import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_excel(r"C:\Users\Casa Da Esquina\Desktop\teste.xlsx") #LOCAL E \NOME DO ARQUIVO

plt.pie(x["Salario"], labels= x["Nome"], autopct="%1.2f%%") #TABELA A SER LIDA / (AUTO PCT SIGNIFICA PORCENTAGEM NO GRAFICO


plt.show()

