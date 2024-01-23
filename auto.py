import pyautogui
from time import sleep

# Clicar e digitar nome usuario
pyautogui.click(951,542, duration=0.5)
pyautogui.write('user')
# Clicar e digitar Senha usuario
pyautogui.click(956,575, duration=0.5)
pyautogui.write('123123')
# Clicar em "Entrar"
pyautogui.click(847,615, duration=0.5)


with open('produtos.txt', 'r') as file:
    for linha in file:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        #registrar produto 
        pyautogui.click(648,526, duration=0.5)
        pyautogui.write(produto)
        # resgistrar quantidade
        pyautogui.click(617,558, duration=0.5)
        pyautogui.write(quantidade)
        # registrar preco
        pyautogui.click(594,594, duration=0.5)
        pyautogui.write(preco)
        # clicar para registrar
        pyautogui.click(506,787, duration=0.5)
        sleep(1)