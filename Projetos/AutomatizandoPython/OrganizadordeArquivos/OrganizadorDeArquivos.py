import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys
import threading

# Caminho da pasta a ser monitorada
SOURCE_FOLDER = r"C:\Users\saito\Downloads"

# Dicionário de categorias por tipo de arquivo
FILE_CATEGORIES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Vídeos": [".mp4", ".mov"],
    "Programas": [".exe", ".msi"],
    "Músicas": [".mp3", ".wav"],
    # Adicione mais categorias conforme necessário
}

# Variável global para controlar a execução
running = True

class FileHandler(FileSystemEventHandler):
    """Handler que monitora as mudanças na pasta e organiza os arquivos."""
    
    def on_created(self, event):
        """Disparado quando um novo arquivo é adicionado à pasta."""
        if not event.is_directory:
            file_path = event.src_path
            file_name = os.path.basename(file_path)
            file_extension = os.path.splitext(file_name)[1].lower()

            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(SOURCE_FOLDER, category)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(destination_folder, file_name))
                    print(f"Arquivo {file_name} movido para {category}")
                    break

def organize_files():
    """
    Organiza os arquivos na pasta de origem conforme suas extensões.
    """
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(SOURCE_FOLDER, category)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
                    print(f"Arquivo {filename} movido para {category}")
                    break

def start_monitoring():
    """
    Inicia a monitoração da pasta em tempo real.
    """
    observer = Observer()
    event_handler = FileHandler()
    observer.schedule(event_handler, SOURCE_FOLDER, recursive=False)
    observer.start()

    print("Monitoramento iniciado. Pressione 'q' e Enter para sair.")

    try:
        while running:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()

def input_thread():
    global running
    while True:
        if input().lower() == 'q':
            running = False
            break

if __name__ == "__main__":
    threading.Thread(target=input_thread, daemon=True).start()
    start_monitoring()
    print("Programa encerrado.")
