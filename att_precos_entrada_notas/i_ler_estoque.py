import pygetwindow as gw
import pyautogui
import pytesseract
from PIL import ImageGrab
import time
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\DEV\Tesseract\tesseract.exe"

# Região da coluna "Qtde em estoque" da linha RF PEÇAS - PI
REGIAO_ESTOQUE = (760, 492, 900, 516)  # altura 24px, centralizado no valor

def executar():
    nome_janela = "C-Plus Nuvem"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.3)

        # Clica na aba Estoque
        ################ NOTEBOOK ################
        pyautogui.moveTo(359, 420)
        pyautogui.click()
        time.sleep(1.5)

        # OCR na região do estoque
        img = ImageGrab.grab(bbox=REGIAO_ESTOQUE)
        img.save(r"C:\DEV\Bot\fotos\estoque_atual.png")
        img = img.resize((img.width * 3, img.height * 3))

        config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789,.'
        texto = pytesseract.image_to_string(img, config=config)
        print(f"🔍 OCR estoque bruto: {repr(texto)}")

        # Pega o primeiro número encontrado (quantidade da RF PEÇAS - PI)
        numeros = re.findall(r'\d+(?:[.,]\d+)?', texto)

        if not numeros:
            print("⚠️ Não foi possível ler o estoque. Assumindo estoque = 0.")
            return 0

        try:
            estoque = float(numeros[0].replace(",", "."))
            print(f"📦 Estoque RF PEÇAS - PI: {estoque}")
            return estoque
        except ValueError:
            print("⚠️ Erro ao converter estoque. Assumindo 0.")
            return 0

    except IndexError:
        print("❌ Janela do CPlus não encontrada.")
        return 0