import pyautogui
import time

print("Posicione o mouse na peça desejada...")
time.sleep(5)  # Tempo pra você mover o mouse até a peça

x, y = pyautogui.position()
print(f"Posição do mouse: x={x}, y={y}")
