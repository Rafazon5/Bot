import time
import threading
import keyboard

from cotacao_mossoro.referencias import executar as referencias
from cotacao_mossoro.busca_cplus import executar as busca

# Número de peças a serem processadas
NUMERO_PECAS = 10
parar = False  # Flag para controle com F1

# Thread para escutar a tecla F1
def escutar_f1():
    global parar
    while not parar:
        if keyboard.is_pressed('f1'):
            parar = True
            print("\n🛑 F1 pressionado. Parando automação...")
            break
        time.sleep(0.1)

# Lógica por peça
def executar_etapas(indice):
    print(f"\n🔁 Iniciando peça {indice + 1} de {NUMERO_PECAS}...\n")
    
    # Primeiro: buscar referências (e colar no obs se precisar)
    busca()
    
    # Depois: (futuro) confirmar estoque e preço

    print(f"✅ Peça {indice + 1} finalizada.\n")

# Execução principal
if __name__ == "__main__":
    print("💡 Pressione F1 a qualquer momento para parar a automação.")

    # Captura as referências antes do loop
    referencias()

    # Inicia a thread que escuta F1
    escuta_thread = threading.Thread(target=escutar_f1, daemon=True)
    escuta_thread.start()

    for i in range(NUMERO_PECAS):
        if parar:
            break
        executar_etapas(i)

    print("🏁 Cotação Mossoró finalizada.")
