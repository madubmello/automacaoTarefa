import pyautogui as py
import time
import pandas as pd

linkSistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "insiraemailaqui@email.com"
senha = "insirasuasenha"

py.PAUSE = 2 #o progama esperará dois segundos antes de realizar cada linha de código da biblioteca

#ENTRANDO NO SISTEMA
py.click(x=111, y=1054) #click no ícone de pesquisa de apps do computador
py.write("Google") #digitando o nome do app que desejamos que seja aberto
py.press("enter") #selecionando o Google Chrome
time.sleep(5) #esperando o computador abrir o Chrome
py.write(linkSistema)
py.press("enter")

#FAZENDO LOGIN NO SISTEMA
py.click(x=797, y=564) #clicando no campo de e-mail
py.write(email) #escrevendo o e-mail (alterar as informações na atribuição da própria variável para facilitar a usabilidade do código)
py.press("tab") #clicando no campo de senha
py.write(senha) #escrevendo a senha 
py.press("enter")

#IMPORTANDO A BASE DE DADOS
planilha = pd.read_csv("produtos.csv")

#CADASTRANDO PRODUTOS
for linha in planilha.index: #ou seja, para cada linha das linhas da planilha
    py.click(x=800, y=385) #clicando no campo "Código do Produto"
    py.write(str(planilha.loc[linha, "codigo"])) #escrevendo o código do produto
    py.press("tab")
    py.write(str(planilha.loc[linha, "marca"])) #escrevendo a marca do produto
    py.press("tab") 
    py.write(str(planilha.loc[linha, "tipo"])) #escrevendo o tipo do produto
    py.press("tab") 
    py.write(str(planilha.loc[linha, "categoria"])) #escrevendo a categoria do produto
    py.press("tab") 
    py.write(str(planilha.loc[linha, "preco_unitario"])) #escrevendo o preço do produto
    py.press("tab") 
    py.write(str(planilha.loc[linha, "custo"])) #escrevendo o custo do produto
    py.press("tab") 

    if not pd.isna(planilha.loc[linha, "obs"]): #se a coluna "obs" não estivar vazia, escrever a observação
        py.write(str(planilha.loc[linha, "obs"])) #escrevendo a observação do produto

    py.press("enter") #submetendo os dados do produto (apertando o botão de envio)

    py.scroll(5000) #voltando até o topo do página para cadastrar o próximo produto