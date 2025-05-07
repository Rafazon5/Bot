import pygetwindow as gw
import pyautogui
import time
import pyperclip
import math
from . import dados_compartilhados

def arredondar_cima_0_05(valor):
    return math.ceil(valor * 20) / 20

def executar():
    nome_janela = "C-Plus Nuvem"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.1)

        # ST
        pyautogui.moveTo(812, 553, duration=0.2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite("15,5")
        print("ST preenchido com sucesso.")

        # LC
        pyautogui.moveTo(1194, 650, duration=0.1)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite("30")
        print("Lucro sobre custo preenchido com sucesso.")

        # Copiar o preço de venda calculado
        pyautogui.moveTo(1279, 681, duration=0.1)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        valor_cplus = pyperclip.paste()
        preco_cplus = float(valor_cplus.replace(",", "."))
        print(f"💰 Preço calculado (CPlus): {valor_cplus}")

        preco_final = arredondar_cima_0_05(preco_cplus)

        print(f"🧠 [DEBUG] Valor atual de valor_ldb: {dados_compartilhados.valor_ldb}")

        # Se tiver valor do LDB e ele for maior, usa o valor do LDB + 0.05
        if dados_compartilhados.valor_ldb is not None and preco_final < dados_compartilhados.valor_ldb:
            if round(dados_compartilhados.valor_ldb * 100) % 5 == 0:
                valor_final = dados_compartilhados.valor_ldb + 0.05
            else:
                valor_final = arredondar_cima_0_05(dados_compartilhados.valor_ldb)
            print(f"🔁 Atualizando com base no LDB: R$ {valor_final:.2f}")
        else:
            valor_final = preco_final
            print(f"✅ Mantendo valor calculado: R$ {preco_final:.2f}")

        # Atualiza o campo com o preço final
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        preco_formatado = f"{valor_final:.2f}".replace(".", ",")
        pyautogui.typewrite(preco_formatado)
        print(f"📌 Preço final inserido: {preco_formatado}")

        # Confirmar
        pyautogui.moveTo(846, 776, duration=0.2)
        pyautogui.click()
        print("💾 Formatação aplicada com sucesso.")
        pyautogui.press('enter')

    except IndexError:
        print(f"❌ Janela com título '{nome_janela}' não encontrada.")
