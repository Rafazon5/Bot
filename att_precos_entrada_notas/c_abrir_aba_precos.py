#abrir aba preco
import pygetwindow as gw
import pyautogui
import time

def executar():
    # Nome da janela do CPlus
    nome_janela = "C-Plus Nuvem"

    ###########################  NOTEBOOK ##################################################
    try:
        # Focar na janela do CPlus
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()

        # Coordenadas da aba "Preços"
        x_precos = 1766
        y_precos = 448
        #quando ta normal
        # x_precos = 957
        # y_precos = 429
        

        # Clicar na aba Preços
        pyautogui.moveTo(x_precos, y_precos)
        pyautogui.click()
        print("Aba 'Preços' acessada com sucesso.")

        # #clica no + bugado
        # x_abre = 42
        # y_abre = 537
        # # Clica no + normal
        # # x_abre = 44
        # # y_abre = 510
        # pyautogui.moveTo(x_abre, y_abre)
        # pyautogui.click()
        # print(" + acessada com sucesso.")
        # time.sleep(0.3)

        #clica na formatacao bugado
        x_forma = 1466
        y_forma = 614
        #clica na formatacao normal
        # x_forma = 1475
        # y_forma = 594
        pyautogui.moveTo(x_forma, y_forma)
        pyautogui.click()
        print(" formatacao acessada com sucesso.")
        time.sleep(0.4)

    ####################################   MONITOR  ############################################
    # try:
    #     # Focar na janela do CPlus
    #     janela = gw.getWindowsWithTitle(nome_janela)[0]
    #     janela.activate()

    #     # Coordenadas da aba "Preços"
    #     x_precos = 775
    #     y_precos = 338

    #     # Clicar na aba Preços
    #     pyautogui.moveTo(x_precos, y_precos)
    #     pyautogui.click()
    #     print("Aba 'Preços' acessada com sucesso.")

    #     # Clica no +
    #     x_abre = 33
    #     y_abre = 407
    #     pyautogui.moveTo(x_abre, y_abre)
    #     pyautogui.click()
    #     print(" + acessada com sucesso.")
    #     time.sleep(0.3)

    #     #clica na formatacao
    #     x_forma = 1200
    #     y_forma = 470
    #     pyautogui.moveTo(x_forma, y_forma)
    #     pyautogui.click()
    #     print(" formatacao acessada com sucesso.")
    #     time.sleep(0.4)

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
