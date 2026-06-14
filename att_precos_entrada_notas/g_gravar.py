#gravar
import pygetwindow as gw
import pyautogui
import time

def executar():
    # Nome da janela do CPlus
    nome_janela = "C-Plus Nuvem"

    try:
        # Focar na janela do CPlus
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()

        ##################### NOTEBOOK ##############################
        # x = 39
        # y = 121

        ##################### MONITOR ###############################
        x = 31
        y = 96

        pyautogui.moveTo(x, y)
        pyautogui.click()
        print("gravar peça com sucesso.")
        pyautogui.press('enter')

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
        