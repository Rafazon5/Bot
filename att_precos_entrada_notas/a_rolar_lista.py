#rolar lista
import pygetwindow as gw
import pyautogui
import time

def executar():
    nome_janela = "C-Plus Nuvem"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()

        #note
        x = 1891
        y = 708
        # x = 1889
        # y = 523

        #monitor
        # x =   1902 #1889
        # y = 786#571
        
        pyautogui.moveTo(x, y)
        pyautogui.click()

        print("Rolagem bem-sucedida.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")

