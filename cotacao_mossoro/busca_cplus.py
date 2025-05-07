import pygetwindow as gw
import pyautogui
import time
import pyperclip
from . import dados_compartilhados

def executar():
    nome_janela = "C-Plus Nuvem"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(0.5)

        encontrou = False

        for referencia in dados_compartilhados.referencias:
            if encontrou:
                break

            # Vai para o campo de busca
            pyautogui.moveTo(672, 436, duration=0.2)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyperclip.copy(referencia)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            print(f"🔎 Buscando referência: {referencia}")
            time.sleep(1)  # tempo para carregar resultados

            # Pergunta manualmente se achou
            resposta = input(f"👀 Achou a peça com referência '{referencia}'? (s/n): ").strip().lower()

            if resposta == "s":
                print(f"✅ Peça encontrada: {referencia}. Selecionando peça...")
                pyautogui.moveTo(554, 527, duration=0.2)
                pyautogui.click()
                pyautogui.click()
                encontrou = True

        if not encontrou:
            print("🚫 Nenhuma referência encontrada nesta peça.")

    except IndexError:
        print("❌ Janela do CPlus não encontrada.")
