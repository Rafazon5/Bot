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
        time.sleep(1)

        x = 39
        y = 121

        pyautogui.moveTo(x, y, duration=0.3)
        pyautogui.click()
        print("gravar peça com sucesso.")
        pyautogui.press('enter')

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
        