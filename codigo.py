import pyautogui
import time
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto
# pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

# passo1: entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espere 3 segundos
time.sleep(3)


# passo 2: fazer login

#preencher email
pyautogui.click(x=597, y=374)
pyautogui.write("nycolasderik240@gmail.com")

#preencher a senha
pyautogui.press("tab")
pyautogui.write("PenisEnormeEreto")

# botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3 segundos
time.sleep(3)

# passo 3: importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# passo 4: cadastrar um produto
for linha in tabela.index: # para cada linha da minha tabela
    pyautogui.click(x=544, y=255)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") #passar pro proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") #passar pro proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") #passar pro proximo campo
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab") #passar pro proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") #passar pro proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") #passar pro proximo campo
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)

    if obs != "nan":
        pyautogui.write(obs)


    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)   

    marca = "Logitech"
    tipo = "Mouse"
    categoria = "1"  
    preco_unitario = "25.95"
    custo = "6.50"
    obs = ""
# passo 5: repetir para todos os produtos

# pyautogui -> fazer automações com python
