#margens
import pygetwindow as gw
import pyautogui
import pyperclip
import time

def executar():
    # Nome da janela do CPlus
    nome_janela = "C-Plus Nuvem"

    ###################################     NOTEBOOK    ###################################
    # try:
    #     # Focar na janela do CPlus
    #     janela = gw.getWindowsWithTitle(nome_janela)[0]
    #     janela.activate()

    #     # Copiar margem da TABELA GERAL
    #     pyautogui.moveTo(445, 617)
    #     pyautogui.click()
    #     pyautogui.click()
    #     pyautogui.hotkey('ctrl', 'a')
    #     pyautogui.hotkey('ctrl', 'c')
    #     margem_geral = pyperclip.paste()
    #     print(f"Margem da Tabela Geral: {margem_geral}")

    #     # Converte a margem geral para float
    #     margem_geral_float = float(margem_geral.replace(",", "."))

    #     # Define a base da margem da Tabela Geral
    #     base_margem_geral = 30.00

    #     # Calcula o acréscimo real
    #     acrescimo = margem_geral_float - base_margem_geral
    #     print(f"Acréscimo detectado: {acrescimo:.2f}")

    #     # Calcula as margens ajustadas
    #     margens = [
    #         (461, 645, f"{40 + acrescimo:.2f}".replace(".", ",")),  # TAB 02
    #         (461, 674, f"{50 + acrescimo:.2f}".replace(".", ",")),  # TAB 03
    #         (461, 699, f"{20 + acrescimo:.2f}".replace(".", ",")),  # TAB ESP
    #         (461, 729, f"{37 + acrescimo:.2f}".replace(".", ","))   # TAB JB
    #     ]

    #     # Preenche cada campo de margem
    #     for x, y, valor in margens:
    #         pyautogui.moveTo(x, y)
    #         pyautogui.click()
    #         pyautogui.hotkey('ctrl', 'a')
    #         pyautogui.press('backspace')
    #         pyautogui.typewrite(valor)
    #         print(f"Margem {valor} preenchida em ({x}, {y})")

    #     print("Todas as margens preenchidas com sucesso.")

    ##############################  MONITOR     ################################
    try:
        # Focar na janela do CPlus
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()

        # Copiar margem da TABELA GERAL
        pyautogui.moveTo(364, 473)
        pyautogui.click()
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        margem_geral = pyperclip.paste()
        print(f"Margem da Tabela Geral: {margem_geral}")

        # Converte a margem geral para float
        margem_geral_float = float(margem_geral.replace(",", "."))

        # Define a base da margem da Tabela Geral
        base_margem_geral = 30.00

        # Calcula o acréscimo real
        acrescimo = margem_geral_float - base_margem_geral
        print(f"Acréscimo detectado: {acrescimo:.2f}")

        # Calcula as margens ajustadas
        margens = [
            (364, 496, f"{40 + acrescimo:.2f}".replace(".", ",")),  # TAB 02
            (364, 517, f"{50 + acrescimo:.2f}".replace(".", ",")),  # TAB 03
            (364, 536, f"{20 + acrescimo:.2f}".replace(".", ",")),  # TAB ESP
            (364, 559, f"{37 + acrescimo:.2f}".replace(".", ","))   # TAB JB
        ]

        # Preenche cada campo de margem
        for x, y, valor in margens:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.typewrite(valor)
            print(f"Margem {valor} preenchida em ({x}, {y})")

        print("Todas as margens preenchidas com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")

if __name__ == "__main__":
    executar()
