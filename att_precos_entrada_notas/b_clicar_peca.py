#clicar peca
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

        #####Mover o mousee até a peça e clicar
        ############################# NOTEBOOK ######################################
        pyautogui.moveTo(124, 449)
        # pyautogui.moveTo(344, 471)
        # pyautogui.moveTo(108, 504)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.moveTo(555, 122)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.moveTo(599, 241)
        pyautogui.click()
        time.sleep(0.1)
        print("Clique realizado na primeira peça com sucesso.")

        ############################# monitor #####################################
        # pyautogui.moveTo(253, 360)
        # pyautogui.click()
        # time.sleep(0.3)
        # pyautogui.moveTo(445, 101)
        # pyautogui.click()
        # time.sleep(0.2)
        # pyautogui.moveTo(464, 196)
        # pyautogui.click()
        # time.sleep(0.1)
        # print("Clique realizado na primeira peça com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
        
# Teste individual:
if __name__ == "__main__":
    executar()    