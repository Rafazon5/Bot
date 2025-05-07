import pygetwindow as gw
import pyautogui
import pyperclip
import time

def executar():
    # Nome da janela do CPlus
    nome_janela = "C-Plus Nuvem"

    try:
        # Focar na janela do CPlus
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.1)

        # Copiar margem da TABELA GERAL
        pyautogui.moveTo(449, 591, duration=0.1)
        pyautogui.click()
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
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
            (452, 623, f"{40 + acrescimo:.2f}".replace(".", ",")),  # TAB 02
            (452, 651, f"{50 + acrescimo:.2f}".replace(".", ",")),  # TAB 03
            (457, 681, f"{20 + acrescimo:.2f}".replace(".", ",")),  # TAB ESP
            (455, 701, f"{37 + acrescimo:.2f}".replace(".", ","))   # TAB JB
        ]

        # Preenche cada campo de margem
        for x, y, valor in margens:
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            pyautogui.typewrite(valor)
            print(f"Margem {valor} preenchida em ({x}, {y})")
            time.sleep(0.1)

        print("Todas as margens preenchidas com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
