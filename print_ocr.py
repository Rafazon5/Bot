# import pyautogui
# import time

# print("Posicione o mouse na peça desejada...")
# time.sleep(5)  # Tempo pra você mover o mouse até a peça

# x, y = pyautogui.position()
# print(f"Posição do mouse: x={x}, y={y}")

# posicao_mouse.py - Cole isso no arquivo existente
import pyautogui
import time
import pyperclip
from PIL import ImageGrab

print("🖱️  Mova o mouse até o PREÇO no LDB e pressione Ctrl+C para capturar.")
print("    Pressione Ctrl+Z para sair.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"\r📍 Posição atual: X={x}, Y={y}   ", end="", flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n\n✅ Posição final capturada!")
    x, y = pyautogui.position()
    print(f"   X={x}, Y={y}")
    
    # Tira screenshot de uma região ao redor do mouse (200x60 pixels)
    margem_x, margem_y = 200, 30
    regiao = (x - margem_x, y - margem_y, x + margem_x, y + margem_y)
    screenshot = ImageGrab.grab(bbox=regiao)
    screenshot.save("posicao.png")
    print(f"\n📸 Screenshot salva em: posicao.png")
    print(f"   Região capturada: left={regiao[0]}, top={regiao[1]}, width=200, height=60")
    print(f"\n💡 Use esses valores no h_busca_ldb.py:")
    print(f"   REGIAO_OCR = ({regiao[0]}, {regiao[1]}, {regiao[0]+200}, {regiao[1]+60})")
