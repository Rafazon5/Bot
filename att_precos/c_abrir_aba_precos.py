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
        time.sleep(0.1)

        # Coordenadas da aba "Preços"
        x_precos = 954
        y_precos = 424

        # Clicar na aba Preços
        pyautogui.moveTo(x_precos, y_precos, duration=0.2)
        pyautogui.click()
        print("Aba 'Preços' acessada com sucesso.")

        # Clica no +
        x_abre = 42
        y_abre = 510
        pyautogui.moveTo(x_abre, y_abre, duration=0.2)
        pyautogui.click()
        print(" + acessada com sucesso.")

        #clica na formatacao
        x_forma = 1527
        y_forma = 594
        pyautogui.moveTo(x_forma, y_forma, duration=0.2)
        pyautogui.click()
        print(" formatacao acessada com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
