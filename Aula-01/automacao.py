#Passo-a-Passo
#Passo 01 -> Abrir o navegador
#Passo 02 -> Acessar o site do sistema com login e senha
#Passo 03 -> Inserir todas as informações do produto
#Passo 04 -> Enviar as informações para o sistema   
#Passo 05 -> Repetir o cadastro até acabar o cadastro de todos os produtos

import pyautogui
import pandas as pd
import time

#Importando o banco de dados
tabela = pd.read_csv("produtos.csv")

pyautogui.PAUSE = 0.5 #Pausando o pyautogui

#Abrindo o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

pyautogui.sleep(0.5) #Adicionando um tempo de espera

#Acessando o site do sistema com login e senha
pyautogui.click(x=1729, y=359)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.sleep(1.0)

#Repetindo até acabar o cadastro de todos os produtos

for linha in tabela.index: #Laço de repetição
    pyautogui.click(x=1702, y=238) #Clicando no primeiro campo

    pyautogui.write(str(tabela.loc[linha, "codigo"])) #Percorrrendo o banco e adicionando o primeiro produto referente a coluna "codigo"
    pyautogui.press("tab") #Pulando para o proximo campo

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Condição da coluna "obs"
    if not pd.isna(tabela.loc[linha, "obs"]): #verificando se a coluna "obs" contém informação
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    #Pulando para o botão     
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000) #Subindo a tela até o início

    


    






