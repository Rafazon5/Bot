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

        # Mover o mouse até a peça e clicar
        pyautogui.moveTo(634, 417, duration=0.1)
        pyautogui.click()
        pyautogui.click()
        print("Clique realizado na primeira peça com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
        
# Teste individual:
if __name__ == "__main__":
    executar()    