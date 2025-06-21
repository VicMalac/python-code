import os
import time
import subprocess

def resetar_spooler():
    print("Parando o serviço de spooler de impressão...")
    subprocess.call(["net", "stop", "spooler"])

    print("Limpando arquivos da fila de impressão...")
    caminho_spool = r"C:\Windows\System32\spool\PRINTERS"
    try:
        for arquivo in os.listdir(caminho_spool):
            caminho_arquivo = os.path.join(caminho_spool, arquivo)
            os.remove(caminho_arquivo)
        print("Fila limpa com sucesso.")
    except Exception as e:
        print(f"Erro ao limpar fila: {e}")

    print("Reiniciando o serviço de spooler de impressão...")
    subprocess.call(["net", "start", "spooler"])
    print("Serviço reiniciado.")

if __name__ == "__main__":
    resetar_spooler()
