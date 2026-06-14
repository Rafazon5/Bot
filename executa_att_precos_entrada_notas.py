import time
import keyboard
import pygetwindow as gw

from att_precos_entrada_notas.a_rolar_lista import executar as rolar
from att_precos_entrada_notas.b_clicar_peca import executar as clicar
from att_precos_entrada_notas.h_busca_ldb import executar as buscar_ldb
from att_precos_entrada_notas.i_ler_estoque import executar as ler_estoque
from att_precos_entrada_notas.j_ler_preco_atual import executar as ler_preco_atual
from att_precos_entrada_notas.j_ler_preco_atual import arredondar_cima_0_05
from att_precos_entrada_notas.c_abrir_aba_precos import executar as abrir_precos
from att_precos_entrada_notas.d_preencher_formatacao_preco import executar as preencher_formatacao
from att_precos_entrada_notas.e_preencher_margens import executar as preencher_margens
from att_precos_entrada_notas.f_ajustar_precos import executar as ajustar_precos
from att_precos_entrada_notas.g_gravar import executar as gravar
from att_precos_entrada_notas import dados_compartilhados

NUMERO_PECAS = 20
parar = False

def escutar_f1():
    global parar
    if keyboard.is_pressed('f1'):
        parar = True
        print("\n🛑 F1 pressionado. Parando automação imediatamente.")
        return True
    return False

def executar_etapas(indice):
    print(f"\n🔁 Iniciando peça {indice + 1} de {NUMERO_PECAS}...\n")

    if escutar_f1(): return

    print("1️⃣  Clicando na peça...")
    clicar()
    time.sleep(4)

    if escutar_f1(): return

    print("📦 Lendo estoque...")
    estoque = ler_estoque()

    if escutar_f1(): return

    print("💰 Lendo preço atual (TAB GERAL)...")
    preco_atual = ler_preco_atual()

    if escutar_f1(): return

    print("🆔 Copiando código e buscando no LDB...")
    buscar_ldb()
    # dados_compartilhados.valor_ldb foi preenchido pelo buscar_ldb()

    # --- LÓGICA DE COMPARAÇÃO ---
    if estoque > 0 and preco_atual is not None:
        preco_novo = dados_compartilhados.preco_calculado  # será preenchido pelo preencher_formatacao
        preco_atual_arredondado = arredondar_cima_0_05(preco_atual)

        print(f"🧠 Estoque: {estoque} | Preço atual: R$ {preco_atual:.2f} | Arredondado: R$ {preco_atual_arredondado:.2f}")

        # Sinaliza para o preencher_formatacao usar no mínimo o preço atual arredondado
        dados_compartilhados.preco_minimo = preco_atual_arredondado
        print(f"🔒 Preço mínimo travado em: R$ {preco_atual_arredondado:.2f} (tem estoque)")
    else:
        dados_compartilhados.preco_minimo = None
        print("🔓 Sem estoque ou preço atual não lido — sem trava de preço mínimo.")

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

    if escutar_f1(): return

    print("5️⃣  Ajustando preços das tabelas...")
    ajustar_precos()

    if escutar_f1(): return

    print("6️⃣  Gravando alterações...")
    gravar()
    time.sleep(4)

    if escutar_f1(): return

    print("7️⃣  Rolando para a próxima peça...")
    rolar()
    time.sleep(1)

    print(f"✅ Peça {indice + 1} finalizada.\n")

if __name__ == "__main__":
    print("💡 Pressione F1 a qualquer momento para parar a automação.")

    while not parar:
        for i in range(NUMERO_PECAS):
            if parar:
                break
            executar_etapas(i)

        if parar:
            break

        try:
            terminal = gw.getWindowsWithTitle("cmd")[0]
            terminal.activate()
            time.sleep(0.5)
        except IndexError:
            print("⚠️ Não foi possível ativar o terminal.")

        resposta = input(f"🔁 Deseja rodar mais {NUMERO_PECAS} peças? (s/n): ").strip().lower()
        if resposta != "s":
            print("🏁 Automação finalizada pelo usuário.")
            break