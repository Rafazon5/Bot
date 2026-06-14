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
        janelas = gw.getWindowsWithTitle(nome_janela)
        if not janelas:
            print("❌ Janela não encontrada.")
            return

        janela = janelas[0]
        janela.activate()
        time.sleep(0.5)

        # ST
        pyautogui.moveTo(812, 553)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite("15,5")
        print("ST preenchido com sucesso.")

        # LC
        pyautogui.moveTo(1194, 650)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.typewrite("30")
        print("Lucro sobre custo preenchido com sucesso.")

        # Copia o preço calculado pelo CPlus
        pyperclip.copy("")
        pyautogui.moveTo(1279, 681)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')

        tentativas = 0
        while not pyperclip.paste() and tentativas < 10:
            time.sleep(0.1)
            tentativas += 1

        valor_bruto = pyperclip.paste().strip()

        if not valor_bruto:
            print("❌ Falha ao copiar o valor (campo vazio).")
            return

        valor_limpo = valor_bruto.replace(".", "").replace(",", ".")
        preco_cplus = float(valor_limpo)
        print(f"💰 Preço calculado (CPlus): {valor_bruto}")

        preco_calculado = arredondar_cima_0_05(preco_cplus)

        print(f"🧠 [DEBUG] valor_ldb: {dados_compartilhados.valor_ldb}")
        print(f"🧠 [DEBUG] preco_minimo: {dados_compartilhados.preco_minimo}")

        # 1. Aplica lógica do LDB
        if dados_compartilhados.valor_ldb is not None and preco_calculado < dados_compartilhados.valor_ldb:
            if round(dados_compartilhados.valor_ldb * 100) % 5 == 0:
                valor_pos_ldb = dados_compartilhados.valor_ldb + 0.05
            else:
                valor_pos_ldb = arredondar_cima_0_05(dados_compartilhados.valor_ldb)
            print(f"🔁 Ajustado pelo LDB: R$ {valor_pos_ldb:.2f}")
        else:
            valor_pos_ldb = preco_calculado
            print(f"✅ Mantendo valor calculado: R$ {preco_calculado:.2f}")

        # 2. Aplica lógica do preço mínimo (estoque > 0)
        if dados_compartilhados.preco_minimo is not None and valor_pos_ldb < dados_compartilhados.preco_minimo:
            valor_final = dados_compartilhados.preco_minimo
            print(f"🔒 Preço travado pelo estoque: R$ {valor_final:.2f} (novo seria R$ {valor_pos_ldb:.2f})")
        else:
            valor_final = valor_pos_ldb
            print(f"✅ Preço final aprovado: R$ {valor_final:.2f}")

        # Salva o preço calculado para referência no main
        dados_compartilhados.preco_calculado = valor_final

        # Insere o preço final no campo
        pyautogui.moveTo(1279, 681)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')

        preco_formatado = f"{valor_final:.2f}".replace(".", ",")
        pyautogui.typewrite(preco_formatado)
        print(f"📌 Preço final inserido: {preco_formatado}")

        # Confirmar
        pyautogui.moveTo(846, 776)
        pyautogui.click()
        print("💾 Formatação aplicada com sucesso.")
        pyautogui.press('enter')

    except Exception as e: 
        print(f"❌ Ocorreu um erro: {e}")