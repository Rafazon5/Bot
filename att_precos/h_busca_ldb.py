import pygetwindow as gw
import pyautogui
import pyperclip
import pytesseract
from PIL import Image
import time
import os
import subprocess
import builtins
#from . 
import dados_compartilhados
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def executar():
    nome_janela = "C-Plus Nuvem"
    ldb = ":: NEW LDB ::"
    try:
        print("\n📄 Copiando código e buscando no LDB...")
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.restore()
        time.sleep(1)
        janela.activate()
        time.sleep(1)

        # Copia o código da peça no CPlus
        pyautogui.moveTo(108, 178, duration=0.2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        codigo = pyperclip.paste()
        print(f"🔗 Código copiado: {codigo}")

        # Vai até o LDB
        newjanela = gw.getWindowsWithTitle(ldb)[0]
        newjanela.restore()
        time.sleep(0.1)
        newjanela.activate()
        time.sleep(0.1)

        # Cola no campo de busca
        pyautogui.moveTo(983, 851, duration=0.2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('enter')
        print("📍 Código colado no campo de busca do LDB.")
        time.sleep(2)

        print("capturando tela")
        screenshot = pyautogui.screenshot(region=(1210, 729, 100, 30))  # x, y, w, h
        texto = pytesseract.image_to_string(screenshot, lang = 'por')
        print(f"texto reconhecido: ´{texto.strip()}")

        # extrai valor numerico
        import re
        match = re.search(r"\d{1,3},\d{2}", texto)
        if match:
            valor = float(match.group(0).replace(",", "."))
            dados_compartilhados.valor_ldb = valor
            print(f"valor do ldb armazenado: R$ {valor:.2f}")
        else:
            dados_compartilhados.valor_ldb = None
            print("nenhum valor valido")

        # try:
        #     terminal = gw.getWindowsWithTitle("cmd")[0]  # ou "PowerShell", "Visual Studio Code", etc.
        #     terminal.activate()
        #     time.sleep(0.5)
        # except IndexError:
        #     print("⚠️ Não foi possível ativar o terminal para digitação.")

        # # Usuário digita o valor do LDB
        # entrada = input("📋 Digite o valor do LDB (ou 'n' se estiver desatualizado ou ausente): ").strip().lower()
        # if entrada != "n":
        #     try:
        #         valor_formatado = float(entrada.replace(",", "."))
        #         dados_compartilhados.valor_ldb = valor_formatado
        #         print(f"💾 Valor do LDB armazenado: R$ {valor_formatado:.2f}")
        #     except ValueError:
        #         dados_compartilhados.valor_ldb = None
        #         print("🚫 Entrada inválida. Nenhum valor armazenado.")
        # else:
        #     dados_compartilhados.valor_ldb = None
        #     print("🚫 Nenhum valor armazenado para essa peça.")

    except IndexError:
        print("❌ Janela do CPlus ou LDB não encontrada.")

if __name__ == "__main__":
    executar()