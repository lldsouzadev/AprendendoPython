import os
import shutil
import tempfile
import datetime
import logging

def setup_logging():
    log_dir = os.path.join(os.path.expanduser("~"), "AutomacaoLogs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, 'limpeza_temp.log')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def limpar_arquivos_temporarios(dias_limite=7, usar_lixeira=True):
    logging.info("Iniciando limpeza de arquivos temporários")
    diretorios = [
        tempfile.gettempdir(),
        os.path.join(os.environ.get('USERPROFILE') or os.environ.get('HOME'), 'Downloads'),
    ]

    lixeira = os.path.join(os.path.expanduser("~"), "Lixeira_Temp")
    if usar_lixeira and not os.path.exists(lixeira):
        os.makedirs(lixeira)

    total_removido = 0
    data_limite = datetime.datetime.now() - datetime.timedelta(days=dias_limite)

    for diretorio in diretorios:
        logging.info(f"Limpando {diretorio}")
        try:
            for item in os.listdir(diretorio):
                item_path = os.path.join(diretorio, item)
                try:
                    if os.path.isfile(item_path):
                        data_modificacao = datetime.datetime.fromtimestamp(os.path.getmtime(item_path))
                        if data_modificacao < data_limite:
                            if usar_lixeira:
                                shutil.move(item_path, os.path.join(lixeira, item))
                                logging.info(f"Movido para lixeira: {item_path}")
                            else:
                                os.unlink(item_path)
                                logging.info(f"Removido: {item_path}")
                            total_removido += 1
                    elif os.path.isdir(item_path):
                        if usar_lixeira:
                            shutil.move(item_path, os.path.join(lixeira, item))
                            logging.info(f"Movido para lixeira: {item_path}")
                        else:
                            shutil.rmtree(item_path)
                            logging.info(f"Removido diretório: {item_path}")
                        total_removido += 1
                except Exception as e:
                    logging.error(f"Erro ao processar {item_path}: {e}")
        except Exception as e:
            logging.error(f"Erro ao acessar {diretorio}: {e}")

    logging.info(f"Limpeza concluída. Total de itens processados: {total_removido}")
    print(f"Limpeza concluída. Total de itens processados: {total_removido}")

if __name__ == "__main__":
    setup_logging()
    limpar_arquivos_temporarios()
    print("Limpeza concluída. Verifique o arquivo de log para mais detalhes.")
