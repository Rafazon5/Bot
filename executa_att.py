import time
import threading
import keyboard
import pygetwindow as gw 

# Importações dos módulos
from att_precos.a_rolar_lista import executar as rolar
from att_precos.b_clicar_peca import executar as clicar
from att_precos.h_busca_ldb import executar as buscar_ldb
from att_precos.c_abrir_aba_precos import executar as abrir_precos
from att_precos.d_preencher_formatacao_preco import executar as preencher_formatacao
from att_precos.e_preencher_margens import executar as preencher_margens
from att_precos.f_ajustar_precos import executar as ajustar_precos
from att_precos.g_gravar import executar as gravar

# Número de peças a serem processadas
NUMERO_PECAS = 10
parar = False  # Flag de controle para parar com F1

# Thread para escutar a tecla F1
def escutar_f1():
    global parar
    if keyboard.is_pressed('f1'):
        parar = True
        print("\n🛑 F1 pressionado. Parando automação imediatamente.")
        return True
    return False

# Função principal de execução por peça
def executar_etapas(indice):
    print(f"\n🔁 Iniciando peça {indice + 1} de {NUMERO_PECAS}...\n")

    if escutar_f1(): return
    print("1️⃣  Clicando na peça...")
    clicar()
    time.sleep(4)

    if escutar_f1(): return
    print("🆔 Copiando código e buscando no LDB...")
    buscar_ldb()
    time.sleep(2)

    if escutar_f1(): return
    print("2️⃣  Acessando aba de preços...")
    abrir_precos()
    time.sleep(1)

    if escutar_f1(): return
    print("3️⃣  Preenchendo formatação de preço...")
    preencher_formatacao()
    time.sleep(0.5)

    if escutar_f1(): return
    print("4️⃣  Preenchendo margens...")
    preencher_margens()
    time.sleep(0.1)

    if escutar_f1(): return
    print("5️⃣  Ajustando preços das tabelas...")
    ajustar_precos()
    time.sleep(0.1)

    if escutar_f1(): return
    print("6️⃣  Gravando alterações...")
    gravar()
    time.sleep(3)

    if escutar_f1(): return
    print("7️⃣  Rolando para a próxima peça...")
    rolar()
    time.sleep(1)

    print(f"✅ Peça {indice + 1} finalizada.\n")

# Execução principal
if __name__ == "__main__":
    print("💡 Pressione F1 a qualquer momento para parar a automação.")

    # Inicia a thread que escuta o F1
    while not parar:
        for i in range(NUMERO_PECAS):
            if parar:
                break
            executar_etapas(i)

        if parar:
            break

        try:
            terminal = gw.getWindowsWithTitle("cmd")[0]  # ou PowerShell, etc.
            terminal.activate()
            time.sleep(0.5)
        except IndexError:
            print("⚠️ Não foi possível ativar o terminal para digitação.")

        resposta = input("🔁 Deseja rodar mais 10 peças? (s para sim / n para não): ").strip().lower()
        if resposta != "s":
            print("🏁 Automação finalizada pelo usuário.")
            break