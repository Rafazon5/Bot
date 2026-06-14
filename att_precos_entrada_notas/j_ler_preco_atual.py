import pygetwindow as gw
import pyautogui
import pytesseract
from PIL import ImageGrab
import time
import re
import math

pytesseract.pytesseract.tesseract_cmd = r"C:\DEV\Tesseract\tesseract.exe"

# Região da coluna "Preço" na linha TAB GERAL (após expandir o +)
REGIAO_PRECO_ATUAL = (591, 610, 691, 635)  # de 791 para 691, corta 100px da direita

def arredondar_cima_0_05(valor):
    return math.ceil(valor * 20) / 20

def executar():
    nome_janela = "C-Plus Nuvem"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.3)

        # Clica na aba Fornecedores
        ################ NOTEBOOK ################
        pyautogui.moveTo(1785, 422)
        pyautogui.click()
        time.sleep(0.5)

        # Clica no + da RF PEÇAS - PI para expandir
        pyautogui.moveTo(44, 536)
        pyautogui.click()
        time.sleep(0.8)

        # OCR na região do preço TAB GERAL
        img = ImageGrab.grab(bbox=REGIAO_PRECO_ATUAL)
        img.save(r"C:\DEV\Bot\fotos\ler_preco_atual.png")
        img = img.resize((img.width * 3, img.height * 3))

        config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789,.'
        texto = pytesseract.image_to_string(img, config=config)
        print(f"🔍 OCR preço atual bruto: {repr(texto)}")

        # Pega o primeiro valor no formato 9,99 ou 99,99 ou 999,99
        valores = re.findall(r'\d{1,4}[.,]\d{2}', texto)

        if not valores:
            print("⚠️ Não foi possível ler o preço atual. Retornando None.")
            return None

        preco_str = valores[0].replace(".", "").replace(",", ".")
        try:
            preco = float(preco_str)
            print(f"💰 Preço atual TAB GERAL: R$ {preco:.2f}")
            return preco
        except ValueError:
            print(f"❌ Erro ao converter preço: {valores[0]}")
            return None

    except IndexError:
        print("❌ Janela do CPlus não encontrada.")
        return None