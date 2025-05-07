import os

def exibir_menu():
    print("\n📋 MENU PRINCIPAL DO BOT")
    print("1️⃣  Atualização de Preços")
    print("2️⃣  Cotação Mossoró")
    print("0️⃣  Sair")

def executar_comando(opcao):
    if opcao == "1":
        os.system("python executa_att.py")
    elif opcao == "2":
        os.system("python executa_mossoro.py")
    elif opcao == "0":
        print("👋 Saindo do programa.")
        exit()
    else:
        print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    while True:
        exibir_menu()
        escolha = input("Digite a opção desejada: ").strip()
        executar_comando(escolha)
