from PIL import Image
import os

def salvar_imagem(img, filepath):
    img.save(filepath)

def mostrar_previa(img):
    img.show()

def menu():
    print("\nEscolha uma opção de edição:")
    print("1. Aumentar Contraste")
    print("2. Aumentar Nitidez")
    print("3. Ajustar Brilho")
    print("4. Converter para Escala de Cinza")
    print("5. Rotacionar Imagem")
    print("6. Ambos (Contraste e Nitidez)")
    print("7. Sair")
    opcao = int(input("Digite o número da sua escolha: "))
    return opcao

def obter_diretorio_atual():
    return os.path.dirname(os.path.abspath(__file__))
