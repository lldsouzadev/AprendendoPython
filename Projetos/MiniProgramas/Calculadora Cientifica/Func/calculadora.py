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



# Funções exponenciais #



# Raizes e Potencias #



# Funções de Numeros Complexos #



# Constantes #



# Outras Funções#