#busca_ldb
import pygetwindow as gw
import pyautogui
import pyperclip
import pytesseract
from PIL import ImageGrab
import time
import re
from . import dados_compartilhados

pytesseract.pytesseract.tesseract_cmd = r"C:\DEV\Tesseract\tesseract.exe"

REGIAO_OCR = (1093, 696, 1163, 714)  # bottom de 718 para 708   
REGIAO_GRUPO = (136, 754, 650, 800)    # grupo na tela da peça aberta

def extrair_preco_ldb():
    img = ImageGrab.grab(bbox=REGIAO_OCR)
    img.save(r"C:\DEV\Bot\fotos\debug_ldb.png")
    img = img.resize((img.width * 3, img.height * 3))
    config = r'--oem 3 --psm 7'
    texto = pytesseract.image_to_string(img, config=config)
    print(f"🔍 Texto bruto OCR preço LDB: {repr(texto)}")

    valores = re.findall(r'\d{1,4}[., ]\d{2}', texto)
    if not valores:
        print("⚠️ Nenhum preço encontrado pelo OCR.")
        return None
    primeiro = valores[0].replace(" ", ".").replace(",", ".")
    try:
        return float(primeiro)
    except ValueError:
        return None

def extrair_grupo_ldb():
    img = ImageGrab.grab(bbox=REGIAO_GRUPO)
    img.save(r"C:\DEV\Bot\fotos\grupo.png")
    img = img.resize((img.width * 3, img.height * 3))
    config = r'--oem 3 --psm 6'
    texto = pytesseract.image_to_string(img, config=config)
    print(f"🔍 Texto bruto OCR grupo LDB: {repr(texto)}")
    return texto.upper()

def executar():
    nome_janela = "C-Plus Nuvem"
    ldb = ":: NEW LDB ::"

    try:
        print("\n📄 Copiando código e marca do CPlus...")
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.5)

        # Copia o código principal
        pyautogui.moveTo(108, 178)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        codigo = pyperclip.paste().strip()
        print(f"🔗 Código copiado: {codigo}")

        # Copia a marca
        pyautogui.moveTo(155, 319)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.2)
        marca_cplus = pyperclip.paste().strip().upper()
        print(f"🏷️ Marca copiada: {marca_cplus}")

        # Restaura o código no clipboard
        pyperclip.copy(codigo)

        # Vai até o LDB
        newjanela = gw.getWindowsWithTitle(ldb)[0]
        newjanela.activate()
        time.sleep(0.3)

        # Pesquisa o código
        pyautogui.moveTo(729, 899, duration=0.2)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.press('enter')
        print("📍 Código colado no campo de busca do LDB.")
        time.sleep(2.5)

        # Abre a peça selecionada
        pyautogui.press('enter')
        time.sleep(1)

        # OCR no grupo
        grupo_ldb = extrair_grupo_ldb()
        print(f"📦 Grupo LDB: {grupo_ldb.strip()}")

        # Volta para a lista
        pyautogui.press('enter')
        time.sleep(0.5)

        # Lê o preço na lista e verifica a marca
        if marca_cplus and marca_cplus in grupo_ldb:
            print(f"✅ Marca '{marca_cplus}' encontrada no grupo LDB.")
            valor = extrair_preco_ldb()
            if valor is not None:
                dados_compartilhados.valor_ldb = valor
                print(f"✅ Valor LDB: R$ {valor:.2f}")
            else:
                dados_compartilhados.valor_ldb = None
                print("⚠️ OCR não leu o preço. LDB ignorado.")
        else:
            dados_compartilhados.valor_ldb = None
            print(f"⚠️ Marca '{marca_cplus}' NÃO encontrada no grupo '{grupo_ldb.strip()}'. LDB ignorado.")

    except IndexError:
        print("❌ Janela do CPlus ou LDB não encontrada.")

if __name__ == "__main__":
    executar()