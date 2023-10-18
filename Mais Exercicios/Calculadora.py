from funcoes import funcoesCalculadora
import time

def main():
    while True:
        escolha = funcoesCalculadora.exibir_menu()
        
        if escolha not in ['1', '2', '3', '4', '5', '6', '7']:
            print('\033[1;31;40m' + 'Opção inválida! Por favor, escolha uma opção válida.' + '\033[0m')
            continue
        
        if escolha == '7':
            break
        
        num1 = float(input('\033[1;32;40m' + 'Digite o primeiro número: ' + '\033[0m'))
        
        if escolha != '6':
            num2 = float(input('\033[1;32;40m' + 'Digite o segundo número: ' + '\033[0m'))
        
        if escolha == '1':
            resultado = funcoesCalculadora.adicao(num1, num2)
            print('\033[1;31;40m' + f'Resultado: {resultado}' + '\033[0m')
        elif escolha == '2':
            resultado = funcoesCalculadora.subtracao(num1, num2)
            print('\033[1;31;40m' + f'Resultado: {resultado}' + '\033[0m')
        elif escolha == '3':
            resultado = funcoesCalculadora.multiplicacao(num1, num2)
            print('\033[1;31;40m' + f'Resultado: {resultado}' + '\033[0m')
        elif escolha == '4':
            resultado = funcoesCalculadora.divisao(num1, num2)
            print('\033[1;31;40m' + f'Resultado: {resultado}' + '\033[0m')
        elif escolha == '5':
            resultado = funcoesCalculadora.potencia(num1, num2)
            print('\033[1;31;40m' + f'Resultado: {resultado}' + '\033[0m')
        elif escolha == '6':
            resultado = funcoesCalculadora.raiz_quadrada(num1)
            print('\033[1;31;40m' + f'Resultado: {resultado}' + '\033[0m')
        else:
            print('\033[1;31;40m' + 'Opção inválida!' + '\033[0m')
            
        time.sleep(2)

if __name__ == "__main__":
    main()
