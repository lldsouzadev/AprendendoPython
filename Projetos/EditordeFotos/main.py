import os
from PIL import Image
from photo_editor import (aumentar_contraste, aumentar_nitidez, ajustar_brilho, 
                         converter_cinza, rotacionar_imagem, salvar_imagem, 
                         mostrar_previa, menu)

# Diretório de imagens (alterar para um caminho absoluto temporário se necessário)
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgs')

# Verifique se o diretório existe antes de tentar listar os arquivos
if not os.path.exists(path):
    print(f"O diretório {path} não foi encontrado.")
else:
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        img = Image.open(filepath)
        
        while True:
            opcao = menu()
            
            if opcao == 1:
                img = aumentar_contraste(img)
            elif opcao == 2:
                img = aumentar_nitidez(img)
            elif opcao == 3:
                fator_brilho = float(input("Digite o fator de brilho (ex: 1.5 para aumentar, 0.5 para diminuir): "))
                img = ajustar_brilho(img, fator_brilho)
            elif opcao == 4:
                img = converter_cinza(img)
            elif opcao == 5:
                angulo = int(input("Digite o ângulo de rotação (ex: 90, 180): "))
                img = rotacionar_imagem(img, angulo)
            elif opcao == 6:
                img = aumentar_contraste(img)
                img = aumentar_nitidez(img)
            elif opcao == 7:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
                continue
            
            mostrar_previa(img)
            salvar = input("Deseja salvar a imagem? (s/n): ")
            if salvar.lower() == 's':
                salvar_imagem(img, filepath)
                print(f"Imagem '{filename}' editada e salva com sucesso!")
                break
            else:
                print("Imagem não salva. Continue editando ou escolha 'Sair' para pular para a próxima imagem.")
        
        if opcao == 7:
            break
