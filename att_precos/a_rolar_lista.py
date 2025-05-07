import pygetwindow as gw
import pyautogui
import time

def executar():
    nome_janela = "C-Plus Nuvem"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.1)  # tempo pra garantir que está em foco

        x = 1901
        y = 710
        
        pyautogui.moveTo(x, y, duration=0.1)
        pyautogui.click()

        print("Rolagem bem-sucedida.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")

