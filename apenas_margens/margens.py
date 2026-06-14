import sys
import os

# Garante que o Python encontra o pacote att_precos_entrada_notas
sys.path.insert(0, r"C:\DEV\Bot")

from att_precos_entrada_notas.e_preencher_margens import executar as preencher_margens
from att_precos_entrada_notas.f_ajustar_precos import executar as ajustar_precos
from att_precos_entrada_notas.g_gravar import executar as gravar

if __name__ == "__main__":
    print("▶️  Preenchendo margens...")
    preencher_margens()

    print("\n▶️  Ajustando preços...")
    ajustar_precos()

    print("\n▶️  Gravando...")
    gravar()

    print("\n✅ Concluído!")