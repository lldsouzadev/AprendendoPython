import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette
from Func.calculadora import (
    soma, subtracao, multiplicacao, divisao,
    seno, cosseno, tangente, arcseno, arcocosseno, arcotangente,
    logaritmo, ln, exponencial, potencia, raiz_quadrada,
    raiz_cubica, fatorial, combinacao, permutacao
)

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora Científica')
        self.setFixedSize(500, 700)  # Define um tamanho fixo para evitar redimensionamento excessivo
        self.last_result = False  # Flag para rastrear se o último botão pressionado foi '='
        self.initUI()
        
    def initUI(self):
        # Paleta de cores
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))  # Cor de fundo preta
        self.setPalette(palette)
        
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        # Área de exibição branca
        self.display_area = QWidget()
        self.display_area.setStyleSheet("background-color: white; border-radius: 10px;")
        display_layout = QVBoxLayout()
        display_layout.setContentsMargins(15, 15, 15, 15)  # Espessura ajustada para melhor aparência
        display_layout.setSpacing(5)
        self.display_area.setLayout(display_layout)
        main_layout.addWidget(self.display_area)

        # Exibição da expressão (conta realizada) - no topo
        self.expression_display = QLabel('')
        self.expression_display.setAlignment(Qt.AlignRight | Qt.AlignTop)
        self.expression_display.setFont(QFont('Arial', 14))
        self.expression_display.setStyleSheet("color: rgba(0, 0, 0, 150);")  # Letra menor e translúcida
        display_layout.addWidget(self.expression_display)

        # Exibição do resultado / entrada atual - na parte inferior
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setReadOnly(True)
        self.display.setFont(QFont('Arial', 28))  # Fonte duplicada e maior
        self.display.setStyleSheet("background-color: white;")
        self.display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        display_layout.addWidget(self.display)

        # Layout de botões
        grid = QGridLayout()
        grid.setSpacing(10)
        main_layout.addLayout(grid)

        # Lista de botões conforme a especificação
        nomes_botoes = [
            ('7', '8', '9', '/', 'Sin'),
            ('4', '5', '6', '*', 'cos'),
            ('1', '2', '3', '-', 'tan'),
            ('.', '0', '^', '+', 'C'),
            ('log', 'ln', 'exp', 'e', 'Del'),
            ('(', ')', 'π', '√', '=')
        ]

        # Adicionando os botões ao grid
        for row, botao_row in enumerate(nomes_botoes):
            for col, botao_nome in enumerate(botao_row):
                button = QPushButton(botao_nome)
                button.setFont(QFont('Arial', 18))
                button.setStyleSheet(self.buttonStyle())
                button.setFixedSize(80, 60)
                grid.addWidget(button, row, col)
                button.clicked.connect(self.on_click)

        # Define o tamanho mínimo do grid para evitar elementos mal posicionados
        grid.setSizeConstraint(QGridLayout.SetFixedSize)

    def buttonStyle(self):
        return """
            QPushButton {
                background-color: #FF8C00;
                color: white;
                border: none;
                border-radius: 15px;
            }
            QPushButton:hover {
                background-color: #FFB732;
            }
            QPushButton:pressed {
                background-color: #E07B00;
            }
        """
        
    def on_click(self):
        sender = self.sender().text()
        current = self.display.text()
        expression = self.expression_display.text()

        # **Gerenciamento do Estado Após Resultado**
        # Se o último botão pressionado foi '=', e o usuário pressiona um botão que inicia uma nova expressão,
        # então limpa o display para iniciar uma nova conta
        if self.last_result:
            if sender in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Sin', 'cos', 'tan', 'log', 'ln', 'exp', 'e', 'π', '√', '('):
                self.display.clear()
                self.expression_display.clear()
                self.last_result = False
            elif sender == 'C':
                self.display.clear()
                self.expression_display.clear()
                self.last_result = False

        # **Tratamento dos Botões**
        if sender == 'C':
            self.display.clear()
            self.expression_display.clear()
            self.last_result = False
        elif sender == 'Del':
            self.display.setText(current[:-1])
        elif sender == '=':
            try:
                # Antes de avaliar, verifique e balanceie os parênteses
                balanced_expression = self.balance_parentheses(current)
                
                # Atualiza a exibição da expressão com a conta realizada
                self.expression_display.setText(current)
                
                # Substituir símbolos por funções do módulo calculadora
                expression = balanced_expression
                expression = expression.replace('Sin', 'seno')
                expression = expression.replace('cos', 'cosseno')
                expression = expression.replace('tan', 'tangente')
                expression = expression.replace('√', 'raiz_quadrada')
                expression = expression.replace('^', '**')
                expression = expression.replace('ln', 'ln')
                expression = expression.replace('log', 'logaritmo')
                expression = expression.replace('exp', 'exponencial')
                expression = expression.replace('π', str(math.pi))
                expression = expression.replace('e', str(math.e))
                # Para funções como 'seno', 'cosseno', etc., certifique-se de que estão em minúsculas no módulo
                # Caso contrário, alinhe a nomenclatura

                # Avaliação segura usando eval com funções do calculadora.py
                resultado = eval(expression, {
                    'seno': seno,
                    'cosseno': cosseno,
                    'tangente': tangente,
                    'raiz_quadrada': raiz_quadrada,
                    'logaritmo': logaritmo,
                    'ln': ln,
                    'exponencial': exponencial,
                    'potencia': potencia,
                    'soma': soma,
                    'subtracao': subtracao,
                    'multiplicacao': multiplicacao,
                    'divisao': divisao,
                    # Adicione outras funções conforme necessário
                })
                self.display.setText(str(resultado))
                self.last_result = True  # Define a flag indicando que um resultado foi exibido
            except Exception as e:
                print(f"Erro ao avaliar a expressão: {e}")  # Feedback para depuração
                self.display.setText("Erro")
                self.last_result = False
        elif sender in ('Sin', 'cos', 'tan', 'log', 'ln', 'exp', '√', '^'):
            # Adiciona a função com um parêntese aberto automaticamente
            if sender in ('Sin', 'cos', 'tan', 'log', 'ln', 'exp', '√'):
                self.display.setText(current + sender + '(')
            else:
                self.display.setText(current + sender)
            self.last_result = False
        elif sender in ('π', 'e'):
            # Adiciona os valores de pi e e
            if sender == 'π':
                self.display.setText(current + str(math.pi))
            elif sender == 'e':
                self.display.setText(current + str(math.e))
            self.last_result = False
        elif sender in ('(', ')'):
            self.display.setText(current + sender)
            self.last_result = False
        else:
            # Se o usuário começar a digitar um número ou continuar a expressão
            self.display.setText(current + sender)
            self.last_result = False

    def balance_parentheses(self, expression):
        """Função para balancear os parênteses antes de avaliar."""
        open_parens = expression.count('(')
        close_parens = expression.count(')')
        missing_parens = open_parens - close_parens
        if missing_parens > 0:
            expression += ')' * missing_parens
        return expression

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())