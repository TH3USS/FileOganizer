import os
import shutil

# Caminho da pasta a ser organizada
CAMINHO_PASTA = "SEU_CAMINHO_AQUI"

# Extensões para classificação de arquivos
TIPOS_DE_ARQUIVOS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".mkv", ".avi"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar"],
    "Outros": []
}

# Função para organizar arquivos por extensão
def organizar_arquivos(caminho):
    if not os.path.exists(caminho):
        print("Caminho especificado não existe.")
        return

    # Criar pastas conforme os tipos definidos
    for pasta in TIPOS_DE_ARQUIVOS.keys():
        pasta_destino = os.path.join(caminho, pasta)
        os.makedirs(pasta_destino, exist_ok=True)

    # Organizar arquivos
    for arquivo in os.listdir(caminho):
        caminho_arquivo = os.path.join(caminho, arquivo)

        # Ignorar pastas
        if os.path.isdir(caminho_arquivo):
            continue

        # Identificar a extensão do arquivo
        _, extensao = os.path.splitext(arquivo)
        destino = "Outros"

        # Encontrar a categoria correspondente
        for categoria, extensoes in TIPOS_DE_ARQUIVOS.items():
            if extensao.lower() in extensoes:
                destino = categoria
                break

        # Mover o arquivo para a pasta correta
        destino_arquivo = os.path.join(caminho, destino, arquivo)
        shutil.move(caminho_arquivo, destino_arquivo)
        print(f"Movido: {arquivo} -> {destino}")

if __name__ == "__main__":
    print("Organizador de Arquivos Simples")
    organizar_arquivos(CAMINHO_PASTA)
    print("Organização concluída!")
