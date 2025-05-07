import pygetwindow as gw
import time
from . import dados_compartilhados

def executar():
    # Nome da janela do navegador (ajustável conforme título)
    nome_janela = "Brave"

    try:
        janela = gw.getWindowsWithTitle(nome_janela)[0]
        janela.activate()
        time.sleep(1)
        print(f"🖥️ Janela '{nome_janela}' ativada com sucesso.")

    except IndexError:
        print(f"❌ Janela com título '{nome_janela}' não encontrada.")
        return

    # Coleta das referências
    entrada = input("Digite as referências separadas por espaço, vírgula ou ponto e vírgula: ").strip()

    # Normaliza e separa as referências
    for separador in [",", ";"]:
        entrada = entrada.replace(separador, " ")
    referencias = [ref.strip().upper() for ref in entrada.split() if ref.strip()]

    dados_compartilhados.referencias = referencias
    print(f"🔗 Referências armazenadas: {dados_compartilhados.referencias}")

    # Pergunta se vai colar no OBS
    resposta = input("Deseja colar no OBS a referência que deu certo? (s/n): ").strip().lower()
    dados_compartilhados.colar_obs = (resposta == "s")

    print("✅ Referências capturadas com sucesso.")
    print(f"📦 Variáveis globais: referencias={dados_compartilhados.referencias}, colar_obs={dados_compartilhados.colar_obs}")
