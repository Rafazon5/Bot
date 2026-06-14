import pygetwindow as gw
import pyautogui
import pyperclip
import time
import math

def executar():
    nome_janela = "C-Plus Nuvem"

    def arredondar_cima_0_05(valor):
        return math.ceil(valor * 20) / 20

    try:
        janelas = gw.getWindowsWithTitle(nome_janela)
        if janelas:
            janelas[0].activate()
            time.sleep(0.5)

        precos = [
            ####################    notebok     ##############################
            # (652, 645),  # TAB 2
            # (652, 674),  # TAB 3
            # (652, 699),  # TAB ESP
            # (652, 729)   # TAB JB

            ####################    monitor     ##############################

            (534, 493),  # TAB 2
            (534, 519),  # TAB 3
            (534, 538),  # TAB ESP
            (534, 555)   # TAB JB
        ]

        for x, y in precos:
            # Limpa o clipboard para evitar usar o valor da volta anterior caso a cópia falhe
            pyperclip.copy("") 
            
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.click()
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            
            # Espera até 0.5 segundos para o valor aparecer no clipboard (essencial para Nuvem)
            timeout = 0
            while not pyperclip.paste() and timeout < 5:
                time.sleep(0.1)
                timeout += 1
            
            valor_raw = pyperclip.paste().strip()
            
            # --- MUDANÇA DE SEGURANÇA AQUI ---
            if not valor_raw:
                print(f"Campo na posição {x}, {y} está vazio. Pulando...")
                continue

            # Tratamento Universal: 
            # 1. Remove pontos (se for 1.250,50 vira 1250,50 / se for 9,50 continua 9,50)
            # 2. Troca vírgula por ponto (vira 1250.50 ou 9.50)
            valor_limpo = valor_raw.replace(".", "").replace(",", ".")
            
            try:
                valor_float = float(valor_limpo)
            except ValueError:
                print(f"Não foi possível converter o texto: {valor_raw}")
                continue
            # ---------------------------------

            print(f"Lido: {valor_raw} -> Convertido: {valor_float}")

            valor_ajustado = arredondar_cima_0_05(valor_float)

            # Usamos uma margem pequena para comparar floats (0.001)
            if abs(valor_float - valor_ajustado) < 0.001:
                print(f"Já arredondado: {valor_float:.2f}")
            else:
                novo_valor = f"{valor_ajustado:.2f}".replace(".", ",")
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('backspace')
                pyautogui.typewrite(novo_valor)
                pyautogui.press('enter') # Garante que o sistema aceite o valor
                print(f"Ajustado: {valor_raw} -> {novo_valor}")

        print("Processo finalizado.")

    except Exception as e:
        print(f"Erro inesperado: {e}")
    

# Para rodar, basta chamar executar()

    ########################### MONITOR ######################################
    # try:
    #     precos = [
    #         (534, 493),  # TAB 2
    #         (534, 519),  # TAB 3
    #         (534, 538),  # TAB ESP
    #         (534, 555)   # TAB JB
    #     ]

    #     for x, y in precos:
    #         # Seleciona e copia o preço atual
    #         pyautogui.moveTo(x, y, duration=0.1)
    #         pyautogui.click()
    #         pyautogui.click()
    #         pyautogui.hotkey('ctrl', 'a')
    #         pyautogui.hotkey('ctrl', 'c')
    #         valor = pyperclip.paste()
    #         print(f"Preço atual lido: {valor}")

    #         # Converte para float e arredonda
    #         valor_float = float(valor.replace(",", "."))
    #         valor_ajustado = arredondar_cima_0_05(valor_float)

    #         if round(valor_float, 2) == round(valor_ajustado, 2):
    #             print(f"Preço já está arredondado: {valor_float:.2f}")
    #         else:
    #             # Substitui o valor no campo
    #             novo_valor = f"{valor_ajustado:.2f}".replace(".", ",")
    #             pyautogui.click()
    #             pyautogui.hotkey('ctrl', 'a')
    #             pyautogui.press('backspace')
    #             pyautogui.typewrite(novo_valor)
    #             print(f"Preço ajustado para: {novo_valor}")

    #     print("Preços ajustados com sucesso.")

    except IndexError:
        print(f"Janela com título '{nome_janela}' não encontrada.")

if __name__ == "__main__":
    executar()
