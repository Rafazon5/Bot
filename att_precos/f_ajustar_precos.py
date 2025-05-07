import pygetwindow as gw
import pyautogui
import pyperclip
import time
import math

def executar():
    # Nome da janela do CPlus
    nome_janela = "C-Plus Nuvem"

    def arredondar_cima_0_05(valor):
        return math.ceil(valor * 20) / 20

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.1)

        precos = [
            (641, 622),  # TAB 2
            (646, 654),  # TAB 3
            (654, 671),  # TAB ESP
            (634, 702)   # TAB JB
        ]

        for x, y in precos:
            # Seleciona e copia o preço atual
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.click()
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.1)
            valor = pyperclip.paste()
            print(f"Preço atual lido: {valor}")

            # Converte para float e arredonda
            valor_float = float(valor.replace(",", "."))
            valor_ajustado = arredondar_cima_0_05(valor_float)

            if round(valor_float, 2) == round(valor_ajustado, 2):
                print(f"Preço já está arredondado: {valor_float:.2f}")
            else:
                # Substitui o valor no campo
                novo_valor = f"{valor_ajustado:.2f}".replace(".", ",")
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                pyautogui.typewrite(novo_valor)
                print(f"Preço ajustado para: {novo_valor}")

            time.sleep(0.1)

        print("Preços ajustados com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")
