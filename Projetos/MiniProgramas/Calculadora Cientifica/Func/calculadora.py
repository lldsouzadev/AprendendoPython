import math

# Funções básicas #

def soma(a, b):
    try:
        return a + b
    except Exception as e:
        return f"Erro: {str(e)}"

def subtracao(a, b):
    try:
        return a - b
    except Exception as e:
        return f"Erro: {str(e)}"

def multiplicacao(a, b):
    try:
        return a * b
    except Exception as e:
        return f"Erro: {str(e)}"

def divisao(a, b):
    try:
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    except Exception as e:
        return f"Erro: {str(e)}"

# Funções trigonométricas #

def seno(a):
    try:
        return math.sin(math.radians(a))
    except Exception as e:
        return f"Erro: {str(e)}"

def cosseno(a):
    try:
        return math.cos(math.radians(a))
    except Exception as e:
        return f"Erro: {str(e)}"

def tangente(a):
    try:
        return math.tan(math.radians(a))
    except Exception as e:
        return f"Erro: {str(e)}"

# Funções trigonométricas inversas #

def arcseno(a):
    try:
        return math.degrees(math.asin(a))
    except Exception as e:
        return f"Erro: {str(e)}"

def arcocosseno(a):
    try:
        return math.degrees(math.acos(a))
    except Exception as e:
        return f"Erro: {str(e)}"

def arcotangente(a):
    try:
        return math.degrees(math.atan(a))
    except Exception as e:
        return f"Erro: {str(e)}"
    
# Funções hiperbólicas #

def seno_hiperbolico(a):
    try:
        return math.sinh(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def cosseno_hiperbolico(a):
    try:
        return math.cosh(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def tangente_hiperbolica(a):
    try:
        return math.tanh(a)
    except Exception as e:
        return f"Erro: {str(e)}"
    
# Funções hiperbólicas inversas#

def arcseno_hiperbolico(a):
    try:
        return math.asinh(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def arcocosseno_hiperbolico(a):
    try:
        return math.acosh(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def arcotangente_hiperbolica(a):
    try:
        return math.atanh(a)
    except Exception as e:
        return f"Erro: {str(e)}"
    
# Funções logarítmicas #

def logaritmo(a, base=10):
    try:
        return math.log(a, base)
    except Exception as e:
        return f"Erro: {str(e)}"

def ln(a):
    try:
        return math.log(a)
    except Exception as e:
        return f"Erro: {str(e)}"

# Funções exponenciais #

def exponencial(a):
    try:
        return math.exp(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def potencia(a, b):
    try:
        return math.pow(a, b)
    except Exception as e:
        return f"Erro: {str(e)}"

# Raízes e Potências #

def raiz_quadrada(a):
    try:
        return math.sqrt(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def raiz_cubica(a):
    try:
        return math.pow(a, 1/3)
    except Exception as e:
        return f"Erro: {str(e)}"

# Funções de Números Complexos #

def parte_real(a, b):
    try:
        return a.real
    except Exception as e:
        return f"Erro: {str(e)}"

def parte_imaginaria(a, b):
    try:
        return a.imag
    except Exception as e:
        return f"Erro: {str(e)}"

def conjugado(a):
    try:
        return a.conjugate()
    except Exception as e:
        return f"Erro: {str(e)}"

# Constantes #

PI = math.pi
E = math.e
GRAUS_PARA_RADIANOS = math.radians(1)
RADIANOS_PARA_GRAUS = math.degrees(1)

# Outras Funções#

def fatorial(a):
    try:
        return math.factorial(a)
    except Exception as e:
        return f"Erro: {str(e)}"

def combinacao(n, k):
    try:
        return math.comb(n, k)
    except Exception as e:
        return f"Erro: {str(e)}"

def permutacao(n, k):
    try:
        return math.perm(n, k)
    except Exception as e:
        return f"Erro: {str(e)}"